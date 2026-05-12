from random import randint


numero1 = int(input("Ingrese limite inferior "))
numero2 = int(input("Ingrese limite superior "))
numero=randint(numero1, numero2)

while numero % 2 != 0:   #LO HIZO EL PROFE :(
    numero=randint(numero1, numero2)
print(numero)

intentos=0

while intentos<3:

    intentos=intentos+1
    numero_user= int(input("Por favor adivine el número "))
    
    if numero_user < numero:
        print("El numero es mayor")
    elif numero_user > numero:
        print("El numero es menor")
    else:
        print(f"Acertaste con {intentos} intentos")
        break

if numero_user!=numero:
    print(f"Perdiste con {intentos} intentos")
    