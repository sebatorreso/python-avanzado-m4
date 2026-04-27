from catalogo import Catalogo
from usuarios import Admin, Cliente
from excepciones import ArchivoError


def main():
    print("=== Bienvenido al Ecommerce ===")

    # se carga el catalogo al inicio
    try:
        catalogo = Catalogo()
    except ArchivoError as e:
        print(f"No se pudo cargar el catalogo: {e}")
        return

    while True:
        print("\nCon que rol quieres ingresar?")
        print("1. Admin")
        print("2. Cliente")
        print("0. Salir")
        opcion = input("Elige una opcion: ").strip()

        if opcion == "0":
            print("Hasta luego!")
            break
        elif opcion == "1" or opcion == "2":
            nombre = input("Ingresa tu nombre: ").strip()
            if nombre == "":
                print("El nombre no puede estar vacio.")
                continue

            if opcion == "1":
                usuario = Admin(nombre)
            else:
                usuario = Cliente(nombre)

            usuario.mostrar_bienvenida()
            usuario.menu(catalogo)
        else:
            print("Opcion no valida.")


main()
