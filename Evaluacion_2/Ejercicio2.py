from random import randint



numero1 = int(input("Ingrese limite inferior "))
numero2 = int(input("Ingrese limite superior "))
numero=randint(numero1, numero2)

if numero % 2 != 0:   #LO HIZO EL PROFE :(
    numero=numero+1
print(numero)

numero_user= int(input("Por favor adivine el número "))
intentos=0

while intentos<3:
    if numero_user < numero:
        intentos=intentos+1
        print("El numero es mayor")
        numero_user= int(input("Por favor adivine el número "))
    elif numero_user > numero:
        intentos=intentos+1
        print("El numero es menor")
        numero_user= int(input("Por favor adivine el número "))