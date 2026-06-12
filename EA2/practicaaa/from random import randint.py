from random import randint

limite_inferior = int(input("ingrese numero inferior"))
limite_superior = int(input("ingrese numero superior"))

contador_de_intentos = 0
intento_guardado_1 = 0
intento_guardado_2 = 0

numero_aleatorio_generado = randint(limite_inferior, limite_superior)

if numero_aleatorio_generado % 2 != 0:
    if numero_aleatorio_generado == limite_superior:
        numero_aleatorio_generado = numero_aleatorio_generado - 1
    else:
        numero_aleatorio_generado = numero_aleatorio_generado + 1
    else:

for numero_de_vueltas in range (1,4):
    intento_adivinanza = int(input("intente adivinar"))
    if intento_adivinanza == numero_aleatorio_generado:
        print("haz adivinado")
        break
    elif intento_adivinanza != numero_aleatorio_generado:
        print("te equivocaste")
        contador_de_intentos += 1
        intento_guardado_1 = intento_adivinanza
        if contador_de_intentos ==0:
            
        if intento_guardado_1 < numero_aleatorio_generado:
            print("el numero es mayor")
        else:
            print("el numero es menor")

                
