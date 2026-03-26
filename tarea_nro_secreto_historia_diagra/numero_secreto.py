numero_secreto = 5
numero_elegido = 0
print("Adivina el numero secreto")
numero_elegido = int(input("eliga un numero"))

while numero_secreto != numero_elegido :
    numero_elegido = int(input(f"Número elegido {numero_elegido} es incorrecto. Ingrese otro numero"))
    if numero_elegido ==  numero_secreto :
        if numero_elegido == numero_secreto :
            break
print ("¡Felicidades, adivinaste el nùmero!")