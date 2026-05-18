from random import randint

num1 = int(input("Ingrese numero minimo: "))
num2 = int(input("Ingrese numero maximo: "))

numero = randint(num1, num2)

if numero // numero == 0:
    numero_final = numero
    print(numero_final)

contador_de_intentos = 0

gurdado1_de_adivinando_el_numero = 0
gurdado2_de_adivinando_el_numero = 0

while True:
    adivinando_el_numero = int(input("Adivina el número secreto del 1 al 10: "))

    if adivinando_el_numero > numero_final:
        print("El numero es menor")
        if contador_de_intentos == 1:
            gurdado2_de_adivinando_el_numero = adivinando_el_numero
            print("Te daré una Pista: ")
        elif contador_de_intentos == 2:
            print("Perdiste")
            break 
        gurdado1_de_adivinando_el_numero = adivinando_el_numero
    
    elif adivinando_el_numero < numero_final:
        print("El numero es mayor")
        if contador_de_intentos == 1:
            gurdado2_de_adivinando_el_numero = adivinando_el_numero
        print("Te daré una Pista: ")
        
        if contador_de_intentos == 2:
            print("Perdiste")
            break
        gurdado1_de_adivinando_el_numero = adivinando_el_numero
    
    elif adivinando_el_numero == numero_final:
        if contador_de_intentos == 0:
            print("Felicitaciones, adivinó en el primer intento.")
            break
        elif contador_de_intentos == 1:
            print("Felicitaciones, adivinó en su segundo intento.")
            break
        else:
            print("Felicitaciones, pudiste adivinar.")
            break
    contador_de_intentos += 1