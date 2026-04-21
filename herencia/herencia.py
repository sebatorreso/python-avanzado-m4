# HERENCIA


class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def respirar(self):
        print("Respirando ando")

class Perro(Animal):
    def ladrar(self):
        print("Guau Guau")


firulais = Perro('Firulais')
firulais.respirar()
firulais.ladrar()


# Polimorfismo

class Ave:
    def volar(self):
        print('Ando volando')

class Aguila(Ave):
    def volar(self):
        print('Ando volando soy un águila')


# isinstance()

class Pago:
    def __init__(self, monto):
        self.monto = monto 

class Efectivo(Pago):
    pass

class Tarjeta(Pago):
    pass

class Cheque(Pago):
    pass 


pagare = Pago(100)
cheque1 =  Cheque(1200)


def verificar_pago(obj):
    if not isinstance(obj, Pago):
        print("Este objeto no es un pago válido")
    elif isinstance(obj, Efectivo):
        print("Abriendo caja manual")
    elif isinstance(obj, Tarjeta):
        print("Pasando la Redbank")
    elif isinstance(obj, Cheque):
        print("Mandando a banco")

verificar_pago(cheque1)



# super()

class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario 

class Desarrollador(Empleado):
    def __init__(self, nombre, salario, lenguaje):
        super().__init__(nombre, salario) # Nos traemos todos los atributos de empleado y agregamoslos que son de desarrollador solamente
        self.lenguaje = lenguaje 


