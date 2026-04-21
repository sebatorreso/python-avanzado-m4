


class Motor:
    def __init__(self, tipo):
        self.tipo = tipo

class Auto:
    def __init__(self, patente, motor):
        self.patente = patente
        self.motor = motor  # Composicion

class Cliente:
    def __init__(self, nombre): #Asociacion
        self.nombre = nombre 
        self.autos = []

    def __str__(self):
        return f"{self.nombre}"

    def agregar_autos(self, auto):
        self.autos.append(auto)

class Mecanico:
    def __init__(self, nombre):
        self.nombre = nombre 

    def reparar_auto(self, auto):
        return print(f"Reparando auto")
    
class Reparacion:
    def __init__(self, auto, mecanico):
        self.auto = auto
        self.mecanico = mecanico 

    def __str__(self):
        return f"{self.mecanico.nombre} está reparando el auto {self.auto.patente} con motor {self.auto.motor}"


cliente1 = Cliente('Pedro')
print(cliente1)

motor = Motor('6 en linea')

auto1 = Auto('xx3434', motor)
print(auto1)

mecanico1 = Mecanico('Federico')
print(mecanico1)

reparacion1 = Reparacion(auto1, mecanico1)
print(reparacion1)