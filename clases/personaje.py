
class Personaje:
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida


mi_personaje = Personaje('Demonetz', 10, 1, 5, 100)

print(f"El nombre del personaje es {mi_personaje.nombre}")
print(f"La fuerza del personaje es de {mi_personaje.fuerza}")