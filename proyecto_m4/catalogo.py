import csv
import os
from excepciones import ProductoNoEncontradoError, ArchivoError

ARCHIVO_CATALOGO = "catalogo.csv"


class Producto:
    # clase que representa un producto del catalogo
    def __init__(self, producto_id, nombre, categoria, precio):
        self.producto_id = str(producto_id).strip()
        self.nombre = nombre.strip()
        self.categoria = categoria.strip()
        self.precio = float(precio)

    def __str__(self):
        return f"[{self.producto_id}] {self.nombre} - Categoria: {self.categoria} - Precio: ${self.precio:.2f}"


class Catalogo:
    # el catalogo contiene todos los productos disponibles
    def __init__(self):
        self.productos = {}
        self._cargar_productos()

    def _cargar_productos(self):
        # intenta leer el catalogo desde el archivo, si no existe carga datos de ejemplo
        if not os.path.exists(ARCHIVO_CATALOGO):
            self._datos_de_ejemplo()
            return
        try:
            archivo = open(ARCHIVO_CATALOGO, newline="", encoding="utf-8")
            lector = csv.DictReader(archivo)
            for fila in lector:
                p = Producto(fila["id"], fila["nombre"], fila["categoria"], fila["precio"])
                self.productos[p.producto_id] = p
            archivo.close()
            if len(self.productos) == 0:
                self._datos_de_ejemplo()
        except OSError as e:
            raise ArchivoError(ARCHIVO_CATALOGO, str(e))

    def _datos_de_ejemplo(self):
        # productos con los que arranca el sistema
        lista = [
            ("P001", "Laptop Lenovo 15", "Tecnologia", 699990),
            ("P002", "Mouse Inalambrico", "Tecnologia", 19990),
            ("P003", "Teclado Mecanico", "Tecnologia", 49990),
            ("P004", "Silla Ergonomica", "Muebles", 149990),
            ("P005", "Escritorio Plegable", "Muebles", 89990),
            ("P006", "Audifonos Sony", "Audio", 249990),
            ("P007", "Webcam 1080p", "Tecnologia", 39990),
            ("P008", "Lampara LED", "Iluminacion", 14990),
        ]
        for id_, nombre, cat, precio in lista:
            p = Producto(id_, nombre, cat, precio)
            self.productos[p.producto_id] = p

    def listar(self):
        return list(self.productos.values())

    def buscar(self, termino):
        termino = termino.lower()
        resultados = []
        for p in self.productos.values():
            if termino in p.nombre.lower() or termino in p.categoria.lower():
                resultados.append(p)
        return resultados

    def obtener(self, producto_id):
        producto = self.productos.get(str(producto_id).strip())
        if producto is None:
            raise ProductoNoEncontradoError(producto_id)
        return producto

    def agregar_producto(self, producto):
        self.productos[producto.producto_id] = producto

    def actualizar_producto(self, producto_id, nombre=None, categoria=None, precio=None):
        producto = self.obtener(producto_id)
        if nombre:
            producto.nombre = nombre.strip()
        if categoria:
            producto.categoria = categoria.strip()
        if precio is not None:
            producto.precio = float(precio)

    def eliminar_producto(self, producto_id):
        self.obtener(producto_id)
        del self.productos[str(producto_id).strip()]

    def guardar_en_archivo(self):
        try:
            archivo = open(ARCHIVO_CATALOGO, "w", newline="", encoding="utf-8")
            campos = ["id", "nombre", "categoria", "precio"]
            escritor = csv.DictWriter(archivo, fieldnames=campos)
            escritor.writeheader()
            for p in self.productos.values():
                escritor.writerow({
                    "id": p.producto_id,
                    "nombre": p.nombre,
                    "categoria": p.categoria,
                    "precio": p.precio
                })
            archivo.close()
            print(f"Catalogo guardado en '{ARCHIVO_CATALOGO}'.")
        except OSError as e:
            raise ArchivoError(ARCHIVO_CATALOGO, str(e))
