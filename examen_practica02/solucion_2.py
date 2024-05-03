class Persona:
    nombre="NOMBRE"
    saldo=0
    def __init__(self, nombre,saldo,cantidad):
        self.nombre = nombre
        self.__saldo = saldo
        self.cantidad = cantidad
    def atributos(self):
        try :
            self.nombre=str(input("Nombre: "))
            self.saldo=int(input("Saldo: "))
            self.cantidad=int(input("Cantidad a añadir: "))
        except TypeError:
            print("El valor ingresado no es valido")
        #print("Nombre :",self.nombre)
        #print("Edad :",self.edad)
        print("Saldo : $",self.saldo)

    def transferencia(self):
        self.__saldo += self.cantidad
        return self.__saldo
    def mostrar_saldo(self):
        print(self.__saldo)
class Empleado(Persona):
    def __init__(self,nombre,saldo,cantidad):
        super().__init__(saldo,cantidad)

persona1=Empleado("<NAME>",200,100)
persona1.atributos()
persona1.transferencia()
persona1.mostrar_saldo()






