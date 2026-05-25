num1 = int(input("Ingrese limite inferior: "))
num2 = int(input("Ingrese limite superior: "))

from random import randint
numero = randint(num1, num2)

intentos = 4

if numero > 10:
    numero_final = numero + 1
elif numero < 10:
    numero_final = numero - 1

while True:
    intentos -= 1
    if intentos == 2 and numero_final > num_usuario:
        print("El número es mayor")
    elif intentos == 2 and numero_final < num_usuario:
        print("El número es menor")

    if intentos == 1 and numero_final > num_usuario2:
        if numero_final - num_usuario2 > numero_final - num_usuario:
            print(f"El intento más cercano al numero es {num_usuario} ")
        elif numero_final - num_usuario2 < numero_final - num_usuario:
            print(f"El intento más cercano al numero es {num_usuario2} ")
        print(f"El número es mayor,")
        
    elif intentos == 1 and numero_final < num_usuario2:
        if numero_final - num_usuario2 > numero_final - num_usuario:
            print(f"El intento más cercano al numero es {num_usuario} ")
        elif numero_final - num_usuario2 < numero_final - num_usuario:
            print(f"El intento más cercano al numero es {num_usuario2} ")
        print(f"El número es menor,")

    if intentos == 0:
        print(f"Perdiste el numero era {numero_final}")
        break

    
    print(f"Tiene {intentos} intentos")
    if intentos == 3:
        num_usuario = int(input("Trate de adivinar: "))
        if num_usuario == numero_final:
            print(f"Felicidades a ganado te sobraron {intentos} intento ")
            break
    elif intentos == 2:
        num_usuario2 = int(input("Trate de adivinar: "))
        if num_usuario2 == numero_final:
            print(f"Felicidades a ganado te sobraron {intentos} intento ")
            break
    elif intentos == 1:
        num_usuario3 = int(input("Trate de adivinar: "))
        if num_usuario3 == numero_final:
            print(f"Felicidades a ganado te sobraron {intentos} intento ")
            break
