import random

def listaAleatorios():
      lista = [0]*10
      for i in range(10):
          lista[i] = random.randint(0, 20)
      return print(lista)


def no_repite(listaAleatorios):
    def no_repite1():
        i=0
        while listaAleatorios[i] == listaAleatorios[i+1]:
            listaAleatorios.remove(listaAleatorios[i])
            if  listaAleatorios[i] != listaAleatorios[i+1]:
                listaAleatorios.append(listaAleatorios[i])
            i=i+1
    return listaAleatorios


def orden(listaAleatorios):
    listaAleatorios.sort(listaAleatorios)
    print(listaAleatorios)
    listaAleatorios.reverse(listaAleatorios)
    print(listaAleatorios)
    return listaAleatorios

def mayor_par(listaAleatorios):
    for i in listaAleatorios:
        if i > listaAleatorios[i]:
            listaAleatorios.remove(listaAleatorios[i])
            return print(listaAleatorios[i])





