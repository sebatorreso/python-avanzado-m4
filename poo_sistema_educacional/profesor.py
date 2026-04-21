from persona import Persona

# CLASE PROFESOR
class Profesor(Persona):
    def __init__(self, rut, nombre, apellido, email, fechaNacimiento, codigoProfesor, especialidad, horasContrato, titulo):
        super().__init__(rut, nombre, apellido, email, fechaNacimiento)
        self.__codigoProfesor = codigoProfesor
        self.__especialidad = especialidad
        self.__horasContrato = horasContrato
        self.__titulo = titulo
        self.cursos = []
 
    def dictarClase(self, curso):
        print("Profesor dictando clase en", curso.getIdCurso())
 
    def registrarNota(self, alumno, nota):
        alumno.notas.append(nota)
        print("Nota", nota, "registrada")
 
    def getAsignacionCurso(self):
        return self.cursos
 
    def crearEvaluacion(self, idEval, tipo, fecha, ponderacion, puntajeMax):
        from clases import Evaluacion
        eva = Evaluacion(idEval, tipo, fecha, ponderacion, puntajeMax)
        print("Evaluacion", tipo, "creada")
        return eva
 
    # sobrecarga: con anio o sin anio
    def getHorario(self, anio=None):
        if anio == None:
            print("Todos los cursos del profesor")
        else:
            print("Cursos del año", anio)
        return self.cursos
 
    # polimorfismo
    def getDatosPersonales(self):
        super().getDatosPersonales()
        print("Codigo:", self.__codigoProfesor)
        print("Especialidad:", self.__especialidad)
        print("Horas contrato:", self.__horasContrato)
        print("Titulo:", self.__titulo)