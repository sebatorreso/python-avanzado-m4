from excepciones import CantidadInvalidaError, CarritoVacioError, ArchivoError
from datetime import datetime

ARCHIVO_ORDENES = "ordenes.txt"


class ItemCarrito:
    # representa un producto dentro del carrito con su cantidad
    def __init__(self, producto, cantidad):
        self.producto = producto
        self.cantidad = cantidad

    def subtotal(self):
        return self.producto.precio * self.cantidad


class Carrito:
    # el carrito guarda los productos que el cliente quiere comprar
    def __init__(self):
        self.items = {}

    def agregar(self, producto, cantidad):
        if not isinstance(cantidad, int) or cantidad <= 0:
            raise CantidadInvalidaError(cantidad)
        # si el producto ya esta en el carrito, suma la cantidad
        if producto.producto_id in self.items:
            self.items[producto.producto_id].cantidad += cantidad
        else:
            self.items[producto.producto_id] = ItemCarrito(producto, cantidad)

    def calcular_total(self):
        total = 0
        for item in self.items.values():
            total += item.subtotal()
        return total

    def esta_vacio(self):
        return len(self.items) == 0

    def vaciar(self):
        self.items = {}

    def mostrar(self):
        if self.esta_vacio():
            print("El carrito esta vacio.")
            return
        print("\n--- Carrito ---")
        for item in self.items.values():
            print(f"  {item.producto.nombre} | Cantidad: {item.cantidad} | Precio unitario: ${item.producto.precio:.2f} | Subtotal: ${item.subtotal():.2f}")
        print(f"  Total a pagar: ${self.calcular_total():.2f}")
        print("---------------")

    def confirmar_compra(self, nombre_cliente):
        if self.esta_vacio():
            raise CarritoVacioError()

        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        try:
            archivo = open(ARCHIVO_ORDENES, "a", encoding="utf-8")
            archivo.write("=== ORDEN DE COMPRA ===\n")
            archivo.write(f"Fecha: {fecha}\n")
            archivo.write(f"Cliente: {nombre_cliente}\n")
            archivo.write("Productos:\n")
            for item in self.items.values():
                archivo.write(f"  - {item.producto.nombre} x{item.cantidad} = ${item.subtotal():.2f}\n")
            archivo.write(f"Total: ${self.calcular_total():.2f}\n")
            archivo.write("=======================\n\n")
            archivo.close()
            print(f"Compra confirmada. La orden fue guardada en '{ARCHIVO_ORDENES}'.")
        except OSError as e:
            raise ArchivoError(ARCHIVO_ORDENES, str(e))
        finally:
            # se vacia el carrito siempre, aunque haya fallado el archivo
            self.vaciar()
