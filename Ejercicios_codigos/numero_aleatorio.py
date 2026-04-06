numero_secreto= 39
numero_elegido= 0
contador= 0

print("========HOLA, BIENVENIDO A ADIVINA EL NUMERO=======")
numero_elegido= int(input("Ingresa un numero: "))

while numero_secreto != numero_elegido:
    if numero_elegido < numero_secreto:
        print("Lo siento, no adivinaste")
        print("El numero es mas grande")
        contador = contador + 1
        numero_elegido= int(input("Intentalo de nuevo: "))
    else:
        print("Lo siento, no adivinaste")
        print("El numero es mas pequeño")
        contador = contador + 1
        numero_elegido= int(input("Intentalo de nuevo: "))

print(f"FELICIDADES, GANASTE EN {contador} INTENTOS!")