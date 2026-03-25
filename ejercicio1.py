import time
import sys
import os
import random

def escribir(texto, velocidad=0.05):
    sys.stdout.write
    for letra in texto:
        sys.stdout.write(letra)
        sys.stdout.flush()
        time.sleep(velocidad)


def limpiar():
    os.system('cls' if os.name == 'nt' else 'clear')


numero_secreto = random.randint(0, 10)

while True:
    limpiar()
    escribir("Adivina el número secreto del 1 al 10 \n")
    eleccion = int(input("Escribe tu número: "))
    if eleccion == numero_secreto:
        time.sleep(1)
        escribir(f"Felicidades el número correcto es: {numero_secreto}")
        break
    else:
        escribir(f"El número secreto no es {eleccion}, Vuelve a intentarlo.")
        time.sleep(2)
        limpiar()