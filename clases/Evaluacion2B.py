from random import randint

numero_aleatorio_generado = randint(1, 10)
limite_inferior = int(input("Ingrese el numero inferior: "))
limite_superior = int(input("Ingrese el numero superior: "))
numero_aleatorio_generado = randint(limite_inferior )
intento_1_guardado = 0
intento_2_guardado = 0

if numero_aleatorio_generado % 2 != 0:

    if numero_aleatorio_generado == limite_superior:
        numero_aleatorio_generado -= 1
    elif numero_aleatorio_generado != limite_superior:
        numero_aleatorio_generado += 1

for contador_de_intentos in range(1,4):
    intento_del_usuario = int(input("Intente adivinar"))
    if intento_del_usuario == numero_aleatorio_generado:
        print("Adiviniste")
        break
    elif intento_del_usuario != numero_aleatorio_generado:
        print("Fallaste")
        if contador_de_intentos == 0:
            conrador_de_intentos += 1
            intento_1_guardado = intento_del_usuario
            if intento_1_guardado < numero_aleatorio_generado:
                print("El numero aleatorio generado es mayor que el intento")
                if abs(numero_aleatorio_generado - intento_1_guardado ) < abs(numero_aleatorio_generado - intento_2_guardado):
                    print("El intento 2 esta más cerca del nimero aleatorio")
                    print(f"El intento 1 es: {intento_1_guardado}")
                    print(f"El intento 2 es: {intento_2_guardado}")
            else:
                print("El numero aletorio presnete es menor que el intento")
            