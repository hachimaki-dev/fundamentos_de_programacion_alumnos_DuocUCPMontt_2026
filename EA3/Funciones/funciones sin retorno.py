#Sin retorno
#Las funciones son bloques de código independientes, funcionan cuando son llamadas

def saludarCompañero():
    print("Hola")

def saludarCompañeroconParametro(nombre_compañero):
    print(f"Hola, {nombre_compañero}")

contador = 0
while True:
    saludarCompañeroconParametro(f"Manuel {contador}")
    contador += 1