from persona import Persona

# CLASE ALUMNO
class Alumno(Persona):
    def __init__(self, rut, nombre, apellido, email, fechaNacimiento, matricula, anioIngreso, nivelActual):
        super().__init__(rut, nombre, apellido, email, fechaNacimiento)
        self.__matricula = matricula
        self.__anioIngreso = anioIngreso
        self.__nivelActual = nivelActual
        self.__promedio = 0
        self.notas = []
        self.cursos = []


    def inscribirAsignatura(self, curso):
        if curso.verificarCupo():
            self.cursos.append(curso)
            print("Alumno inscrito en curso", curso.getIdCurso())
        else:
            print("No hay cupo disponible")
 

    def calcularPromedio(self):
        if len(self.notas) == 0:
            print("No tiene notas")
            return 0
        suma = 0
        for n in self.notas:
            suma = suma + n
        self.__promedio = suma / len(self.notas)
        return self.__promedio
 

    # sobrecarga: con semestre o sin semestre
    def getHistorialNotas(self, semestre=None):
        if semestre == None:
            return self.notas
        else:
            print("Notas semestre", semestre, ":", self.notas)
            return self.notas
 

    def verHorario(self):
        for c in self.cursos:
            print("Curso:", c.getIdCurso(), "- Sala:", c.getSala())
 

    # polimorfismo: sobreescribe getDatosPersonales de Persona
    def getDatosPersonales(self):
        super().getDatosPersonales()
        print("Matricula:", self.__matricula)
        print("Anio ingreso:", self.__anioIngreso)
        print("Nivel actual:", self.__nivelActual)
        print("Promedio:", self.__promedio)