import json

class Transaccion:

    def __init__(self, monto, descripcion):
        self.__monto = monto 
        self.descripcion = descripcion 

    def get_monto(self):
        return self.__monto 
    
    def set_monto(self, monto):
        if monto > 0:
            self.__monto = monto
        else:
            print("Monto ingresao es 0 o menor")

    def tipo(self):
        return "Transacción"

    def mostrar(self):
        return print(f"{self.descripcion} - {self.get_monto()} - {self.tipo()}")



class Ingreso(Transaccion):
    # Polimorfismo de la clase Transaccion, del método tipo()
    def tipo(self):
        return "Ingreso"


class Egreso(Transaccion):
    # Polimorfismo de la clase Transaccion, del método tipo()
    def tipo(self):
        return "Egreso"



class GestorFinanzas:
    def __init__(self):
        self.transacciones = []

    def agregar(self, *transacciones):
        for transaccion in transacciones:
            if not isinstance(transaccion, Transaccion):
                raise TypeError("Debe ser una transacción válida")
            self.transacciones.append(transaccion)

        print("Transacciones agregadas")

    def mostrar_todo(self):
        if not self.transacciones:
            print('Lista vacía')
        for transaccion in self.transacciones:
            transaccion.mostrar()


    def calcular_balance(self):
        balance = 0
        for transaccion in self.transacciones:
            if isinstance(transaccion, Ingreso):
                balance += transaccion.get_monto()
            else:
                balance -= transaccion.get_monto()
        return balance
        

    def guardar_en_archivo(self, archivo = "archivo.txt"):
        data = [{
            "tipo": transaccion.tipo(),
            "monto": transaccion.get_monto(),
            "descripcion": transaccion.descripcion
        } for transaccion in self.transacciones]

        with open(archivo, "w"):
            pass

    def importar_del_archivo(self):
        pass



pago = Transaccion(100, "Pago de Servicio")


ingreso1 = Ingreso(100, 'Ingreso')
ingreso2 = Ingreso(100, 'Ingreso')
ingreso3 = Ingreso(100, 'Ingreso')
ingreso4 = Ingreso(100, 'Ingreso')
egreso1 = Egreso(50, 'Egreso')
egreso2 = Egreso(50, 'Egreso')
egreso3 = Egreso(50, 'Egreso')
egreso4 = Egreso(50, 'Egreso')


gestor = GestorFinanzas()


gestor.agregar(ingreso1, ingreso2, ingreso3, ingreso4)
gestor.agregar(egreso1, egreso2, egreso3, egreso4)

print(gestor.calcular_balance())
