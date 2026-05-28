from random import randint

def solicitar_limites():
    lim_inferior = 0
    lim_superior = 0

    while lim_inferior >= lim_superior:
        lim_inferior = int(input("Ingrese el límite inferior: "))
        lim_superior = int(input("Ingrese el límite superior: "))

        if lim_inferior >= lim_superior:
            print("El limite inferior debe ser menor al limite superior")

    return lim_inferior, lim_superior

num_aleatorio = randint(solicitar_limites())

if num_aleatorio % 2 == 1:
    if num_aleatorio + 1 <= lim_superior:
        num_aleatorio += 1
    else:
        num_aleatorio -= 1

print("Ingresa el numero a adivinar")

intento = 1
adivinado = False

while intento <= 3 and not adivinado:
    num_ingresado = int(input(f"Intento {intento}: "))

    if num_aleatorio == num_ingresado:
        print("Felicitaciones, pudiste adivinar")
        adivinado = True
    elif intento == 1:
        diferencia_int_1 = abs(num_aleatorio - num_ingresado)

        if num_aleatorio > num_ingresado:
            print(f"El numero aleatorio es mayor que {num_ingresado}")
        else:
            print(f"El numero aleatorio es menor que {num_ingresado}")
    elif intento == 2:
        diferencia_int_2 = abs(num_aleatorio - num_ingresado)

        if num_aleatorio > num_ingresado:
            print(f"El numero aleatorio es mayor que {num_ingresado}")

            if diferencia_int_1 < diferencia_int_2:
                print(f"El numero aleatorio esta mas cerca del numero del primer intento")
            elif diferencia_int_1 > diferencia_int_2:
                print(f"El numero aleatorio esta mas cerca del numero del segundo intento")
            else:
                print(f"El numero aleatorio esta igual de cerca en ambos intentos")
        else:
            print(f"El numero aleatorio es menor que {num_ingresado}")

            if diferencia_int_1 < diferencia_int_2:
                print(f"El numero aleatorio esta mas cerca del numero del primer intento")
            elif diferencia_int_1 > diferencia_int_2:
                print(f"El numero aleatorio esta mas cerca del numero del segundo intento")
            else:
                print(f"El numero aleatorio esta igual de cerca en ambos intentos")
    else:
        print(f"Perdiste, el numero aleatorio era: {num_aleatorio}")

intento += 1