class errores:
    def __init__(self, a,b):
        self.a = a
        self.b = b

    def division(self):
        self.a = int(input("digite un numero: "))
        self.b = int(input("digite un numero: "))
        try:

            resultado = self.a / self.b
            print(resultado)
        except ZeroDivisionError:
            print("No se puede dividir entre cero")
    def suma(self):
        self.a = int(input("digite un numero: "))
        self.b = int(input("digite un numero: "))
        try:
            resultado=self.a+self.b
            print(resultado)
        except TypeError:
            print("No se puede sumar un str con un int")
            print("vuelva a intentarlo")

digite=errores(0,0)
digite.division()
digite.suma()


#errores.suma(1, "hola")
#errores.division(2, 0)
#errores.division(13.4, 5)


