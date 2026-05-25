from random import randint

def numero_generado_y_ajustado(inf, sup):
    if inf > sup:
        inf, sup = sup, inf
    
    numero = randint(inf, sup)

    if numero % 2 != 0:
        if numero + 1 <= sup:
            numero += 1
        elif numero - 1 >= inf:
            numero -= 1
        else:
            return None
    
    return numero

#Inputs de rango
lim_inf = int(input("Ingrese límite inferior: "))
lim_sup = int(input("Ingrese límite superior: "))

numero_par = numero_generado_y_ajustado(lim_inf, lim_sup)

intento_user = 0

respuestas_previas = []


while intento_user < 3:
    intento_user += 1
    
    if intento_user == 1:
        respuesta = int(input("\nIntente adivinar: "))
    elif intento_user == 2:
        respuesta = int(input("\nIntente de nuevo: "))
    else:
        respuesta = int(input("\nIntente la última vez: "))
        
    respuestas_previas.append(respuesta)

    if respuesta == numero_par:
        if intento_user == 1:
            print("Felicitaciones, adivinó en el primer intento.")
        elif intento_user == 2:
            print("Felicitaciones, adivinó en su segundo intento.")
        else:
            print("Felicitaciones, pudiste adivinar.")
        break
        

    if respuesta < numero_par:
        print("El número es mayor.")
    else:
        print("El número es menor.")


    if intento_user == 2:
        print("Te daré una pista:")
        dif1 = abs(respuestas_previas[0] - numero_par)
        dif2 = abs(respuestas_previas[1] - numero_par)
        
        if dif2 < dif1:
            print(f"El número que buscas está más cerca de {respuestas_previas[1]} que de {respuestas_previas[0]}")
        else:
            print(f"El número que buscas está más cerca de {respuestas_previas[0]} que de{respuestas_previas[1]}")

if intento_user == 3 and respuesta != numero_par:
    print("Perdiste.")
    print(f"El número era: {numero_par}")