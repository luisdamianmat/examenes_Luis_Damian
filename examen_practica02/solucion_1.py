from datetime import date
from datetime import datetime
class Persona:
    nombre="NOMBRE"
    edad=0
    saldo=0
    nacionalidad="Peruana"
    def __init__(self, nombre, edad,saldo,nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.saldo = saldo
        self.nacionalidad = nacionalidad
    def atributos(self):
        try :
            self.nombre=str(input("Nombre: "))
            self.edad=int(input("Edad: "))
        except TypeError:
            print("El valor ingresado no es valido")
        #print("Nombre :",self.nombre)
        #print("Edad :",self.edad)
        print("Saldo : $",self.saldo)
        print("Nacionalidad :",self.nacionalidad)

    def cumple(self):
        self.edad=self.edad+1
        print("Edad de cumpleaños aumentada en 1 :",self.edad)

    def registro(self):
        regis = datetime.now()
        print("Fecha registrada: ",regis)

persona1=Persona("",0,2000,"Peruana")
persona1.atributos()
persona1.cumple()
persona1.registro()
"""abajo dejo las instancias de Personas ya probadas"""
#la_persona1=Persona("Juan",15,2000,"Peruana")
#la_persona1.atributos()
#la_persona1.cumple(0)
#la_persona1.atributos()
#la_persona2=Persona("John",19,3000,"Venezolano")
#la_persona2.atributos()
#la_persona2.cumple(0)
#la_persona2.atributos()

