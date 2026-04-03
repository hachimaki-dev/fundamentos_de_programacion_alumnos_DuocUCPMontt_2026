numero_secreto = 7
numero_elegido = 0

while numero_secreto != numero_elegido:
    numero_elegido = int(input("Adivina el numero del 1 al 10: "))
    if numero_secreto != numero_elegido:
        print("Te equivocaste intente nuevamente")

print(f"Adivinaste el numero es {numero_secreto} excelente")
print(f"***Programa finalizado****")