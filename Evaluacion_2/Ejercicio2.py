from random import randint


limite_inferior=int(input("Ingrese limite inferior "))
limite_superior=int(input("Ingrese limite superior "))
numero_aleatorio_generado=randint(limite_inferior, limite_superior)

if numero_aleatorio_generado % 2 != 0:
    numero_aleatorio_generado+=1
# print(numero_aleatorio_generado)
    if numero_aleatorio_generado==limite_superior:
        numero_aleatorio_generado-=1
    elif numero_aleatorio_generado!=limite_superior:
        numero_aleatorio_generado+=1

numero_usuario= int(input("Por favor adivine el número "))
intentos=0

#while intentos<3:
#    if numero_usuario < numero_aleatorio_generado:
#        intentos=intentos+1
#        print("El numero es mayor")
#        numero_usuario= int(input("Por favor adivine el número "))
#    elif numero_usuario > numero_aleatorio_generado:
#        intentos=intentos+1
#        print("El numero es menor")
#        numero_usuario= int(input("Por favor adivine el número "))

cada_vuelta=1

for cada_vuelta in range(1,4):
    intento_usuario= int(input("Intente adivinar "))
    if intento_usuario==numero_aleatorio_generado:
        print("Felicidades, adivinaste el numero")
        break
    else:
        #Se equivoco
        #Vienen las pistas
        if cada_vuelta==1:
            intento_1_fallido=intento_usuario
            contador_intento_fallido+=1
            print("Fallaste")
            if intento_usuario<numero_aleatorio_generado:
                print("El número es mayor")
            elif intento_usuario>numero_aleatorio_generado:
                print("El número es menor")
        elif cada_vuelta==2:
            intento_2_fallido=intento_usuario
            contador_intento_fallido+=1
            print("Fallaste")
            if intento_usuario<numero_aleatorio_generado:
                print("El número es mayor")
                if abs(numero_aleatorio_generado-intento_1_fallido)<abs(numero_aleatorio_generado-intento_2_fallido):
                    print("El primer intento estuvo más cerca")
                    print(f"Recuerda que el número está entre {intento_1_fallido}")
            elif intento_usuario>numero_aleatorio_generado:
                print("El número es menor")
                if abs(numero_aleatorio_generado-intento_1_fallido)<abs(numero_aleatorio_generado-intento_2_fallido):
                    print("El primer intento estuvo más cerca")
                    print(f"Recuerda que el número está entre {intento_1_fallido}")
        elif contador_intento_fallido==2:
            print(f"Fallaste, el número era {numero_aleatorio_generado}")
            break
        