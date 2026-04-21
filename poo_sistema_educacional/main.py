from persona import Persona
from alumno import Alumno
from profesor import Profesor
from directivo import Directivo
from clases import Asignatura, Evaluacion, Horario, Curso, Matricula, Departamento

print("=== SISTEMA EDUCACIONAL ===")
print()

# instanciar objetos
alumno1 = Alumno("12345678-9", "Juan", "Perez", "juan@correo.com", "2003-05-10", "MAT001", 2024, 1)
profesor1 = Profesor("98765432-1", "Maria", "Lopez", "maria@correo.com", "1985-03-22", "P001", "Programacion", 44, "Ing. Civil Informatico")
directivo1 = Directivo("11111111-1", "Carlos", "Gomez", "carlos@correo.com", "1975-08-15", "Director", "Facultad de Ingenieria")

asignatura1 = Asignatura("INF101", "Programacion I", 8, 6, "Introduccion a la programacion")
curso1 = Curso("C001", 2024, 1, 30, "Sala A101")
curso1.asignatura = asignatura1

horario1 = Horario("H001", "Lunes", "08:30", "10:00")
curso1.horarios.append(horario1)

matricula1 = Matricula("M001", "2024-03-01", 1200000)
depto1 = Departamento("D001", "Informatica", 50000000, directivo1)

# polimorfismo
print("--- Polimorfismo (getDatosPersonales) ---")
print()
print("Datos alumno:")
alumno1.getDatosPersonales()
print()
print("Datos profesor:")
profesor1.getDatosPersonales()
print()
print("Datos directivo:")
directivo1.getDatosPersonales()
print()

# sobrecarga de metodos
print("--- Sobrecarga de metodos ---")
print()

alumno1.notas = [5.5, 6.0, 4.8]
print("getHistorialNotas sin parametro:")
print(alumno1.getHistorialNotas())
print("getHistorialNotas con semestre:")
alumno1.getHistorialNotas(1)
print()

evaluacion1 = Evaluacion("E001", "Prueba 1", "2024-04-10", 30, 100)
evaluacion1.calificar(alumno1, 75)
print("esAprobado nota minima 4.0:")
evaluacion1.esAprobado(alumno1)
print("esAprobado nota minima 6.0:")
evaluacion1.esAprobado(alumno1, 6.0)
print()

horario2 = Horario("H002", "Lunes", "09:00", "10:30")
print("haySolapamiento con otro horario:")
horario1.haySolapamiento(otroHorario=horario2)
print("haySolapamiento con horas:")
horario1.haySolapamiento(horaInicio="11:00", horaFin="12:30")
print()

print("generarReporte normal:")
directivo1.generarReporte()
print("generarReporte detallado:")
directivo1.generarReporte(detallado=True)
print()

asig2 = Asignatura("INF100", "Intro Computacion", 4, 3, "Curso base")
print("setPrerequisitos con uno:")
asignatura1.setPrerequisitos(prerequisito=asig2)
print("setPrerequisitos con lista:")
asignatura1.setPrerequisitos(lista=[asig2])
print()

# interaccion entre objetos
print("--- Interaccion entre objetos ---")
print()

directivo1.asignarProfesor(profesor1, curso1)
profesor1.dictarClase(curso1)
alumno1.inscribirAsignatura(curso1)
profesor1.registrarNota(alumno1, 6.5)

promedio = alumno1.calcularPromedio()
print("Promedio:", promedio)

matricula1.registrar(alumno1, curso1)
directivo1.aprobarMatricula(matricula1)
depto1.agregarProfesor(profesor1)

print()
print("Horario del alumno:")
alumno1.verHorario()

print()
print("=== FIN ===")