import sys
import time
import os

rojo = '\033[31m'
amarillo = '\033[33m'
negrita = '\033[1m'
verde = '\033[32m'
cian = '\033[36m'
reset = '\033[0m'

def escribir(texto, velocidad=0.05, nueva_linea=True):
    for letra in texto:
        sys.stdout.write(letra)
        sys.stdout.flush()
        time.sleep(velocidad)
    if nueva_linea:
        print()

def limpiar():
    os.system('cls' if os.name == 'nt' else 'clear')

numero_secreto = 32
numero_usuario = None
intentos = 0

limpiar()
escribir(f"{negrita}{cian}ADIVINA EL NÚMERO SECRETO{reset}")
escribir(f"\n{negrita}{verde}CUAL CREES QUE ES EL NUMERO SECRETO?{reset}")
while numero_usuario != numero_secreto:
    try:
        numero_usuario = int(input(f"ELIGE UN NUMERO DEL {amarillo}1{reset} AL {amarillo}50{reset}: "))
        if numero_usuario > 50:
            intentos += 1
            escribir(f"{negrita}{rojo}PORFAVOR ELIGE UN NUMERO DEL 1 AL 50{reset}\n")
        elif numero_usuario == numero_secreto:
            intentos += 1
            escribir(f"{verde}FELICIDADES, ADIVINASTE EL NUMERO SECRETO EN {cian}{intentos}{verde} INTENTO/S!{reset}")
        elif numero_secreto < numero_usuario:
            intentos += 1
            escribir(f"EL NUMERO SECRETO ES {rojo}MENOR{reset} QUE {numero_usuario}\n")
        else:
            intentos += 1
            escribir(f"EL NUMERO SECRETO ES {rojo}MAYOR{reset} QUE {numero_usuario}\n")
    except ValueError:
        print(f"{rojo}Error: Por favor ingresa un número.{reset}")