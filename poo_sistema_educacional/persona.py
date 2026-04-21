

# CLASE PERSONA
class Persona:
    def __init__(self, rut, nombre, apellido, email, fechaNacimiento):
        self.__rut = rut
        self.__nombre = nombre
        self.__apellido = apellido
        self.__email = email
        self.__fechaNacimiento = fechaNacimiento

    # metodo publico (+)
    def getId(self):
        return self.__rut
    
    # metodo protegido (#)
    def getDatosPersonales(self):
        print("Rut:", self.__rut)
        print("Nombre:", self.__nombre)
        print("Apellido:", self.__apellido)
        print("Email:", self.__email)
        print("Fecha nacimiento:", self.__fechaNacimiento)