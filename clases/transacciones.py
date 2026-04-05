

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
    
    def tipo():
        return "Egreso"



class GestorFinanzas:
    def __init__(self):
        self.transacciones = []

    def agregar(self, transaccion):
        self.transacciones.append(transaccion)

    def mostrar_todo(self):
        if not self.transacciones:
            print('Lista vacía')
        for transaccion in self.transacciones:
            transaccion.mostrar()

    def calcular_balance(self):
        pass

    def guardar_en_archivo(self):
        pass

    def importar_del_archivo(self):
        pass





pago = Transaccion(100, "Pago de Servicio")

gestor = GestorFinanzas()
gestor.agregar(pago)

gestor.mostrar_todo()
