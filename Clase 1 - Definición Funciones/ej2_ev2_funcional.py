# tomar el ej 1 o 2 de la prueba y transformarlo a programacion funcional

from random import randint

def generar_numero():
    limite_inferior = int(input("Ingrese el límite inferior del rango: "))
    limite_superior = int(input("Ingrese el límite superior del rango: "))
    numero_secreto = randint(limite_inferior, limite_superior)
    return numero_secreto, limite_inferior, limite_superior

def convertir_a_numero_par(numero_secreto, limite_superior):
    if numero_secreto % 2 != 0:
        if numero_secreto + 1 <= limite_superior:
            numero_secreto += 1
        else:
            numero_secreto -= 1
    return numero_secreto

numero_intento1 = 0
numero_intento2 = 0
mas_cercano = 0
mas_lejano = 0
intentos = 3

numero_secreto, limite_inferior, limite_superior = generar_numero()
numero_secreto = convertir_a_numero_par(numero_secreto, limite_superior)

while intentos > 0:
    numero_ingresado = int(input(f"Adivine el número par dentro del rango {limite_inferior, limite_superior}: "))
    if numero_ingresado == numero_secreto:
        print("Felicitaciones, pudiste adivinar")
        break
    else:
        intentos -= 1
        if intentos == 2:
            numero_intento1 = numero_ingresado
            if numero_secreto > numero_ingresado:
                print("El número secreto es mayor al número ingresado")
            else:
                print("El número secreto es menor al número ingresado")
        elif intentos == 1:
            numero_intento2 = numero_ingresado
            if abs(numero_secreto - numero_intento1) > abs(numero_secreto - numero_intento2):
                mas_cercano = numero_intento2
                mas_lejano = numero_intento1
            else:
                mas_cercano = numero_intento1
                mas_lejano = numero_intento2            
            if numero_secreto > numero_ingresado:
                print("El número secreto es mayor al número ingresado")
            else:
                print("El número secreto es menor al número ingresado")
            print(f"Te daré una pista: el número que buscas está más cerca de {mas_cercano} que de {mas_lejano}")
        else:
            print(f"No te quedan intentos. Perdiste. El número secreto era {numero_secreto}")  
