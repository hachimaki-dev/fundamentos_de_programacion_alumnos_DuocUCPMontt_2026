numero_secreto = 40
numero_elegido = 0
contador = 1 
while numero_elegido != numero_secreto:
    numero_elegido = int(input("ingrese el numero secreto:"))
    if numero_elegido < numero_secreto:
        print("el numero es mas alto")
        contador = contador + 1
    elif numero_elegido > numero_secreto:
        print("el numero es mas bajo")
        contador = contador + 1
if numero_elegido == numero_secreto:
    print(f"¡ganaste en {contador} intentos!")
