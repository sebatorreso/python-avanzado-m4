# excepciones personalizadas para el ecommerce

class ProductoNoEncontradoError(Exception):
    def __init__(self, producto_id):
        super().__init__(f"No se encontro ningun producto con el id '{producto_id}'.")
        self.producto_id = producto_id


class CantidadInvalidaError(Exception):
    def __init__(self, cantidad):
        super().__init__(f"La cantidad '{cantidad}' no es valida. Tiene que ser un numero entero mayor a 0.")
        self.cantidad = cantidad


class CarritoVacioError(Exception):
    def __init__(self):
        super().__init__("El carrito esta vacio, no se puede confirmar la compra.")


class ArchivoError(Exception):
    def __init__(self, nombre_archivo, detalle=""):
        mensaje = f"Hubo un problema con el archivo '{nombre_archivo}'."
        if detalle:
            mensaje += f" Detalle: {detalle}"
        super().__init__(mensaje)
        self.nombre_archivo = nombre_archivo
