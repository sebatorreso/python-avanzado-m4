
# CLASE LIBRO
# Definición de la clase Libro()
class Libro():
    def __init__(self, titulo, autor, anio_publicacion, nombre_editorial, ciudad_editorial):
        self.__titulo = titulo
        self.__autor = autor
        self.__anio_publicacion = anio_publicacion
        self.__editorial = Editorial(nombre_editorial, ciudad_editorial)  # se crea ADENTRO del constructor de Libro()

    def mostrar_info(self):
        print(f"Título: {self.__titulo}")
        print(f"Autor: {self.__autor.get_nombre()}")
        print(f"País: {self.__autor.get_pais()}")
        print(f"Año: {self.__anio_publicacion}")
        print(f"Editorial: {self.__editorial.get_nombre()}")
        print(f"Ciudad: {self.__editorial.get_ciudad()}")

    # Definción método accesador get_titulo()
    def get_titulo(self):
        return self.__titulo
    
    # Definición método mutador set_titulo()
    def set_titulo(self, nuevo_titulo):
        self.__titulo = nuevo_titulo

    # Definición método accesador get_anio_publicacion()
    def get_anio_publicacion(self):
        return self.__anio_publicacion
    
    # Definición método mutador set_anio_publicacion()
    def set_anio_publicacion(self, nuevo_anio_publicacion):
        if nuevo_anio_publicacion > 0:
            self.__anio_publicacion = nuevo_anio_publicacion
        else:
            print('Año inválido')

    # Método resumen() con sobrecarga simulada
    def resumen(self, texto=None):
        if texto is None:
            print("Libro sin resumen disponible")
        else:
            print(texto)


# CLASE AUTOR
# Definiendo la clase Autor()
class Autor():
    def __init__(self, nombre, pais):
        self.__nombre = nombre
        self.__pais = pais

    def get_nombre(self):
        return self.__nombre

    def get_pais(self):
        return self.__pais



# CLASE EDITORIAL
# Definiendo la clase Editorial()
class Editorial():
    def __init__(self, nombre, ciudad):
        self.__nombre = nombre
        self.__ciudad = ciudad

    def get_nombre(self):
        return self.__nombre

    def get_ciudad(self):
        return self.__ciudad


# Instanciando un objeto - autor1
autor1 = Autor('Saint-Exupery', 'Francia')

# Instanciando un objeto - libro1
libro1 = Libro('El Principito', autor1, 1943, "Conecta", "Chile")

# PARTE 2
# Llamando métodos
print(libro1.get_titulo())
libro1.set_titulo('El principito (edición especial)')
print(libro1.get_titulo())

# PARTE 3
# Simular sobrecarga usando valores por defecto y condicionales en el método
libro1.resumen()
libro1.resumen('Acá va el resumen de El Principito...Acá termina.')

# PARTE 4
# Mostrando información
libro1.mostrar_info()

