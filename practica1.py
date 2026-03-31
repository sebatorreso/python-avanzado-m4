

# CLASE PERSONA TIENE QUE SER EN MAYUSCULA
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola mi nombre es {self.nombre} y tengo {self.edad} años")

    def cumplir_anios(self):
        self.edad = self.edad + 1 


juanito = Persona('Juan', 10)
carlos = Persona('Carlos', 20)

print(juanito.nombre, juanito.edad)
print(carlos.nombre, carlos.edad)


print(juanito.saludar())
print(juanito.cumplir_anios())
print(juanito.saludar())
print(juanito.cumplir_anios())
print(juanito.saludar())