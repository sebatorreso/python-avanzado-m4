# PILARES DE LA POO

class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo

    def __str__(self):
        return f"Esto es el objeto {self.titular} y tiene un saldo de {self.__saldo}"

    def depositar(self, monto):
        if monto > 0:
            self.__saldo += monto 
        

    def retirar(self, monto):
        if self.__saldo > monto:
            self.__saldo -= monto
        else:
            print("Retiro no es posible")
        


cuenta1 = CuentaBancaria("Juan", 10)
cuenta2 = CuentaBancaria("Carlos", 100)


# HERENCIA

class Vehiculo:
    def __init__(self, marca):
        self.marca = marca

    def moverse(self):
        print("¡El auto se movió!")


class Auto(Vehiculo):
    def moverse(self):
        print("Auto moviendose")

class Moto(Vehiculo):
    def moverse(self):
        print("Moto moviendose")


auto1 = Auto('Suzuki')
moto1 = Moto('BMW')

print(moto1.moverse())
print(auto1.moverse())