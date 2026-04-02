# PROGRAMACION ORIENTADA A OBJETOS
# ACTIVIDAD N°1 
# --------------------------------

# 1. EXPLORACIÓN TEÓRICA

# 1.1) ¿Qué es la programación orientada a objetos?
# Es un paradigma de programación que organiza el código en torno a objetos, que combinan datos
# y comportamiento en una sola unidad.

# 1.2) ¿En qué se diferencia de la programación estructurada? y 1.3) Ejemplo de la vida cotidiana reflejando concepto de objeto.
# La estructurada sigue pasos en orden, uno tras otro, y los datos están separados de las instrucciones.
# Mientras que la POO, es como tener un electrodomestico inteligente: una licuadora ya "sabe" que tiene cuchillas
# y motor, también "sabe" cómo licuar, todo junto en un solo aparato. En vez de escribir pasos sueltos, crea objetos
# que representan cosas del mundo real, cada uno con sus propios datos y acciones incluidas.


# Definición de la clase Perro
class Perro():
    def __init__(self, nombre, edad, raza): # Método constructor de la clase para inicializar objetos
        self.nombre = nombre 
        self.edad = edad 
        self.raza = raza

    def ladrar(self):   # Definición de método ladrar()
        return print("¡Guau!")
    

# Instanciando un objeto
mascota1 = Perro('Maximo', 3, 'Pitbull')
print(mascota1.nombre)
print(mascota1.nombre)
print(mascota1.nombre)

# Llamando método ladrar
mascota1.ladrar()


# 3. DIFERENCIAR CONCEPTOS
# 3.1) Diferencia entre -> Clase, instancia y objeto.
# Clase es el molde o plantilla, define cómo será algo, pero no existe en la realidad. Es como el plano de una casa
# El objeto es algo concreto creado a partir de ese molde. Es la casa ya construida, con su dirección, color y estado.
# Instancia es simplementa otra palabra para decir "objeto".

