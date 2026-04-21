from persona import Persona

# CLASE DIRECTIVO
class Directivo(Persona):
    def __init__(self, rut, nombre, apellido, email, fechaNacimiento, cargo, dependencia):
        super().__init__(rut, nombre, apellido, email, fechaNacimiento)
        self.__cargo = cargo
        self.__dependencia = dependencia

    def gestionarPlanta(self):
        print("Gestionando planta docente")

    # sobrecarga: reporte simple o detallado
    def generarReporte(self, detallado=False):
        if detallado == False:
            print("Reporte - Cargo:", self.__cargo)
        else:
            print("Reporte detallado:")
            self.getDatosPersonales()

    def aprobarMatricula(self, matricula):
        matricula.estado = "Aprobada"
        print("Matricula", matricula.getIdMatricula(), "aprobada")

    def asignarProfesor(self, profesor, curso):
        curso.profesor = profesor
        print("Profesor asignado al curso", curso.getIdCurso())

    def getEstadisticas(self):
        print("Cargo:", self.__cargo)
        print("Dependencia:", self.__dependencia)

    # polimorfismo
    def getDatosPersonales(self):
        super().getDatosPersonales()
        print("Cargo:", self.__cargo)
        print("Dependencia:", self.__dependencia)