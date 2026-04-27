from catalogo import Producto
from carrito import Carrito
from excepciones import (
    ProductoNoEncontradoError,
    CantidadInvalidaError,
    CarritoVacioError,
    ArchivoError
)


class Usuario:
    # clase base para admin y cliente
    def __init__(self, nombre, rol):
        self.nombre = nombre
        self.rol = rol

    def mostrar_bienvenida(self):
        print(f"\nBienvenido/a {self.nombre} - rol: {self.rol}")

    def menu(self, catalogo):
        # cada subclase va a tener su propio menu
        pass


class Admin(Usuario):
    # el admin puede gestionar el catalogo
    def __init__(self, nombre):
        super().__init__(nombre, "ADMIN")

    def menu(self, catalogo):
        while True:
            print("\n--- Menu Admin ---")
            print("1. Listar productos")
            print("2. Crear producto")
            print("3. Actualizar producto")
            print("4. Eliminar producto")
            print("5. Guardar catalogo en archivo")
            print("0. Salir")
            opcion = input("Elige una opcion: ").strip()

            if opcion == "0":
                print("Saliendo del menu admin.")
                break
            elif opcion == "1":
                self.listar_productos(catalogo)
            elif opcion == "2":
                self.crear_producto(catalogo)
            elif opcion == "3":
                self.actualizar_producto(catalogo)
            elif opcion == "4":
                self.eliminar_producto(catalogo)
            elif opcion == "5":
                try:
                    catalogo.guardar_en_archivo()
                except ArchivoError as e:
                    print(f"Error: {e}")
            else:
                print("Opcion no valida, intenta de nuevo.")

    def listar_productos(self, catalogo):
        productos = catalogo.listar()
        if len(productos) == 0:
            print("El catalogo esta vacio.")
            return
        print("\n--- Catalogo ---")
        for p in productos:
            print(f"  {p}")
        print("----------------")

    def crear_producto(self, catalogo):
        print("\n-- Nuevo producto --")
        prod_id = input("ID: ").strip()
        nombre = input("Nombre: ").strip()
        categoria = input("Categoria: ").strip()
        precio_str = input("Precio: ").strip()

        if prod_id == "" or nombre == "" or categoria == "" or precio_str == "":
            print("Todos los campos son obligatorios.")
            return

        try:
            precio = float(precio_str)
            if precio < 0:
                print("El precio no puede ser negativo.")
                return
        except ValueError:
            print("El precio ingresado no es valido.")
            return

        # verificar que el id no exista ya
        try:
            catalogo.obtener(prod_id)
            print(f"Ya existe un producto con el id '{prod_id}'.")
            return
        except ProductoNoEncontradoError:
            pass

        catalogo.agregar_producto(Producto(prod_id, nombre, categoria, precio))
        print(f"Producto '{nombre}' agregado.")

    def actualizar_producto(self, catalogo):
        self.listar_productos(catalogo)
        prod_id = input("\nID del producto a actualizar: ").strip()
        try:
            producto = catalogo.obtener(prod_id)
        except ProductoNoEncontradoError as e:
            print(f"Error: {e}")
            return

        print(f"Editando: {producto}")
        print("(Deja en blanco si no quieres cambiar ese campo)")
        nombre = input(f"Nuevo nombre [{producto.nombre}]: ").strip()
        categoria = input(f"Nueva categoria [{producto.categoria}]: ").strip()
        precio_str = input(f"Nuevo precio [{producto.precio:.2f}]: ").strip()

        precio = None
        if precio_str != "":
            try:
                precio = float(precio_str)
                if precio < 0:
                    print("El precio no puede ser negativo.")
                    return
            except ValueError:
                print("El precio ingresado no es valido.")
                return

        catalogo.actualizar_producto(
            prod_id,
            nombre if nombre != "" else None,
            categoria if categoria != "" else None,
            precio
        )
        print("Producto actualizado.")

    def eliminar_producto(self, catalogo):
        self.listar_productos(catalogo)
        prod_id = input("\nID del producto a eliminar: ").strip()
        try:
            producto = catalogo.obtener(prod_id)
        except ProductoNoEncontradoError as e:
            print(f"Error: {e}")
            return
        confirmacion = input(f"Seguro que quieres eliminar '{producto.nombre}'? (s/n): ").strip().lower()
        if confirmacion == "s":
            catalogo.eliminar_producto(prod_id)
            print("Producto eliminado.")
        else:
            print("Operacion cancelada.")


class Cliente(Usuario):
    # el cliente puede ver el catalogo, agregar al carrito y comprar
    def __init__(self, nombre):
        super().__init__(nombre, "CLIENTE")
        self.carrito = Carrito()  # el cliente tiene su propio carrito

    def menu(self, catalogo):
        while True:
            print("\n--- Menu Cliente ---")
            print("1. Ver catalogo")
            print("2. Buscar producto")
            print("3. Agregar al carrito")
            print("4. Ver carrito")
            print("5. Confirmar compra")
            print("0. Salir")
            opcion = input("Elige una opcion: ").strip()

            if opcion == "0":
                print("Saliendo del menu cliente.")
                break
            elif opcion == "1":
                self.ver_catalogo(catalogo)
            elif opcion == "2":
                self.buscar_producto(catalogo)
            elif opcion == "3":
                self.agregar_al_carrito(catalogo)
            elif opcion == "4":
                self.carrito.mostrar()
            elif opcion == "5":
                self.confirmar_compra()
            else:
                print("Opcion no valida, intenta de nuevo.")

    def ver_catalogo(self, catalogo):
        productos = catalogo.listar()
        if len(productos) == 0:
            print("El catalogo esta vacio.")
            return
        print("\n--- Catalogo ---")
        for p in productos:
            print(f"  {p}")
        print("----------------")

    def buscar_producto(self, catalogo):
        termino = input("Ingresa el nombre o categoria a buscar: ").strip()
        if termino == "":
            print("Debes ingresar algo para buscar.")
            return
        resultados = catalogo.buscar(termino)
        if len(resultados) == 0:
            print(f"No se encontraron productos para '{termino}'.")
            return
        print(f"\nResultados para '{termino}':")
        for p in resultados:
            print(f"  {p}")

    def agregar_al_carrito(self, catalogo):
        self.ver_catalogo(catalogo)
        prod_id = input("\nIngresa el ID del producto: ").strip()
        try:
            producto = catalogo.obtener(prod_id)
        except ProductoNoEncontradoError as e:
            print(f"Error: {e}")
            return

        cantidad_str = input(f"Cuantos '{producto.nombre}' quieres agregar?: ").strip()
        try:
            cantidad = int(cantidad_str)
        except ValueError:
            print("La cantidad tiene que ser un numero entero.")
            return

        try:
            self.carrito.agregar(producto, cantidad)
            print(f"Se agrego {cantidad} x '{producto.nombre}' al carrito.")
        except CantidadInvalidaError as e:
            print(f"Error: {e}")

    def confirmar_compra(self):
        self.carrito.mostrar()
        if self.carrito.esta_vacio():
            print("No puedes confirmar una compra con el carrito vacio.")
            return
        confirmacion = input("Confirmar compra? (s/n): ").strip().lower()
        if confirmacion == "s":
            try:
                self.carrito.confirmar_compra(self.nombre)
            except (CarritoVacioError, ArchivoError) as e:
                print(f"Error: {e}")
        else:
            print("Compra cancelada.")
