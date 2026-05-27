from random import randint

limite_inferior = int(input("Ingrese el límite inferior del rango: "))
limite_superior = int(input("Ingrese el límite superior del rango: "))
numero_aleatorio_generado = randint(limite_inferior, limite_superior)
intento_1_guardado = 0
intento_2_guardado = 0

if numero_aleatorio_generado % 2 != 0:
    if numero_aleatorio_generado == limite_superior:
        numero_aleatorio_generado -= 1
    elif numero_aleatorio_generado != limite_superior:
        numero_aleatorio_generado += 1

# Como sabemos la cantidad de vueltas es más conveniente usar for
for contador_de_intentos in range(1,4):
    intento_del_usuario = int(input("Intente adivinar: "))
    if intento_del_usuario == numero_aleatorio_generado:
        print("Adivinaste, eres el mejor <3 tqm")
    elif intento_del_usuario != numero_aleatorio_generado:
        print("Fallaste")
        if contador_de_intentos == 1:
            intento_1_guardado = intento_del_usuario
            if intento_1_guardado < numero_aleatorio_generado:
                print("El numero aleatorio generado es mayor que el intento")
            else:
                print("El numero aleatorio generado es menor que el intento")
        elif contador_de_intentos == 2:
            intento_2_guardado = intento_del_usuario
            if abs(numero_aleatorio_generado - intento_1_guardado) < abs(numero_aleatorio_generado - intento_2_guardado):
                print("El intento 1 esta mas cerca que el intento 2")
                print(f"El intento 1 es {intento_1_guardado}")
                print(f"El intento 2 es {intento_2_guardado}")
            else:
                print("El intento 2 esta mas cerca que el intento 1")
                print(f"El intento 1 es {intento_1_guardado}")
                print(f"El intento 2 es {intento_2_guardado}")
        elif contador_de_intentos == 3:
            print(f"Fallaste. El numero era {numero_aleatorio_generado}")
            break
