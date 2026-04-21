SISTEMA EDUCACIONAL - POO en Python
=====================================

ARCHIVOS
--------
persona.py    -> clase base Persona
alumno.py     -> clase Alumno (hereda de Persona)
profesor.py   -> clase Profesor (hereda de Persona)
directivo.py  -> clase Directivo (hereda de Persona)
clases.py     -> clases Asignatura, Evaluacion, Horario, Curso, Matricula, Departamento
main.py       -> programa principal con ejemplos de uso

COMO EJECUTAR
-------------
1. Tener Python instalado (version 3 en adelante)
2. Poner todos los archivos en una misma carpeta
3. Abrir una terminal en esa carpeta
4. Ejecutar: python main.py

CONCEPTOS IMPLEMENTADOS
------------------------
- Herencia: Alumno, Profesor y Directivo heredan atributos y metodos de Persona
- Polimorfismo: cada subclase sobreescribe el metodo getDatosPersonales()
  mostrando sus propios datos ademas de los de Persona
- Sobrecarga: metodos con parametros opcionales, por ejemplo:
    getHistorialNotas(semestre=None)
    esAprobado(alumno, notaMinima=4.0)
    generarReporte(detallado=False)
- Encapsulamiento: atributos privados con doble guion bajo (self.__atributo)
  y metodos get para acceder a ellos desde afuera
