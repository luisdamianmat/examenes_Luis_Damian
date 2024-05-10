import time

def medir_tiempo(funcion):
    def wrapper(*args, **kwargs):
        start = time.time()
        resultado=funcion(*args,**kwargs)

        print("tipo total:",time.time()-start)
        return resultado
    return wrapper

@medir_tiempo
def suma(a,b):
    time.sleep(2)
    return a+b

print(suma(10,20))
@medir_tiempo
def multiplicacion():
    time.sleep(2)
    a=int(input("ingrese un numero :"))
    b=int(input("ingrese un numero :"))
    c=int(input("ingrese un numero :"))
    d=int(input("ingrese un numero :"))

    multi=a*b*c*d
    return print("la multiplicacion es:" ,multi)

multiplicacion()
