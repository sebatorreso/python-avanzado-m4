

# CLASES; ASIGNATURA, EVALUACION, HORARIO, CURSO, MATRICULA, DEPARTAMENTO
class Asignatura:
    def __init__(self, codigo, nombre, creditos, horas, descripcion):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__creditos = creditos
        self.__horas = horas
        self.__descripcion = descripcion
        self.prerequisitos = []
        self.evaluaciones = []

    def getPrograma(self):
        print("Codigo:", self.__codigo)
        print("Nombre:", self.__nombre)
        print("Creditos:", self.__creditos)
        print("Horas:", self.__horas)
        print("Descripcion:", self.__descripcion)

    def getEvaluaciones(self):
        return self.evaluaciones

    # sobrecarga: un prerequisito o una lista
    def setPrerequisitos(self, prerequisito=None, lista=None):
        if lista != None:
            self.prerequisitos = lista
            print("Prerequisitos agregados")
        elif prerequisito != None:
            self.prerequisitos.append(prerequisito)
            print("Prerequisito agregado")
        else:
            print("No se ingreso prerequisito")


class Evaluacion:
    def __init__(self, idEval, tipo, fecha, ponderacion, puntajeMax):
        self.__idEval = idEval
        self.__tipo = tipo
        self.__fecha = fecha
        self.__ponderacion = ponderacion
        self.__puntajeMax = puntajeMax
        self.resultados = {}

    def calificar(self, alumno, puntaje):
        nota = round((puntaje * 7) / self.__puntajeMax, 1)
        self.resultados[alumno.getId()] = nota
        print("Nota:", nota)
        return nota

    def getResultados(self):
        return self.resultados

    # sobrecarga: nota minima por defecto 4.0
    def esAprobado(self, alumno, notaMinima=4.0):
        if alumno.getId() in self.resultados:
            if self.resultados[alumno.getId()] >= notaMinima:
                print("Alumno aprobado")
                return True
            else:
                print("Alumno reprobado")
                return False
        print("No hay nota para ese alumno")
        return False


class Horario:
    def __init__(self, idHorario, diaSemana, horaInicio, horaFin):
        self.__idHorario = idHorario
        self.__diaSemana = diaSemana
        self.__horaInicio = horaInicio
        self.__horaFin = horaFin
        self.curso = None

    def getBloque(self):
        print(self.__diaSemana, "de", self.__horaInicio, "a", self.__horaFin)

    # sobrecarga: comparar con objeto Horario o con horas sueltas
    def haySolapamiento(self, otroHorario=None, horaInicio=None, horaFin=None):
        if otroHorario != None:
            if self.__diaSemana == otroHorario.__diaSemana:
                if self.__horaInicio < otroHorario.__horaFin and self.__horaFin > otroHorario.__horaInicio:
                    print("Hay solapamiento")
                    return True
            print("No hay solapamiento")
            return False
        elif horaInicio != None and horaFin != None:
            if self.__horaInicio < horaFin and self.__horaFin > horaInicio:
                print("Hay solapamiento")
                return True
            print("No hay solapamiento")
            return False

    def getCurso(self):
        return self.curso


class Curso:
    def __init__(self, idCurso, anio, semestre, cupo, sala):
        self.__idCurso = idCurso
        self.__anio = anio
        self.__semestre = semestre
        self.__cupo = cupo
        self.__sala = sala
        self.profesor = None
        self.alumnos = []
        self.asignatura = None
        self.horarios = []

    def getIdCurso(self):
        return self.__idCurso

    def getSala(self):
        return self.__sala

    def getSemestre(self):
        return self.__semestre

    def getAlumnos(self):
        return self.alumnos

    def getProfesor(self):
        return self.profesor

    def verificarCupo(self):
        if len(self.alumnos) < self.__cupo:
            print("Hay cupo en el curso", self.__idCurso)
            return True
        else:
            print("El curso esta lleno")
            return False


class Matricula:
    def __init__(self, idMatricula, fechaMatricula, montoArancel):
        self.__idMatricula = idMatricula
        self.__fechaMatricula = fechaMatricula
        self.estado = "Pendiente"
        self.__montoArancel = montoArancel
        self.cursos = []

    def getIdMatricula(self):
        return self.__idMatricula

    def registrar(self, alumno, curso):
        alumno.inscribirAsignatura(curso)
        self.cursos.append(curso)
        print("Matricula", self.__idMatricula, "registrada")

    def anular(self):
        self.estado = "Anulada"
        print("Matricula", self.__idMatricula, "anulada")

    # sobrecarga: todos los cursos o filtrar por semestre
    def getCursos(self, semestre=None):
        if semestre == None:
            return self.cursos
        else:
            resultado = []
            for c in self.cursos:
                if c.getSemestre() == semestre:
                    resultado.append(c)
            return resultado


class Departamento:
    def __init__(self, idDpto, nombre, presupuesto, jefe=None):
        self.__idDpto = idDpto
        self.__nombre = nombre
        self.__presupuesto = presupuesto
        self.jefe = jefe
        self.profesores = []
        self.asignaturas = []

    def getProfesores(self):
        return self.profesores

    def getAsignaturas(self):
        return self.asignaturas

    def agregarProfesor(self, profesor):
        self.profesores.append(profesor)
        print("Profesor agregado al departamento", self.__nombre)