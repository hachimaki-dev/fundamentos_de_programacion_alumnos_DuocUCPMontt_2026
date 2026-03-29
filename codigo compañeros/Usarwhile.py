print("***ADIVINA EL NÚMERO")
numero_secreto = 7
numero_adivinado = 0
while numero_secreto != numero_adivinado :
    numero_adivinado = int(input("Escoge un numero entre 1 y 10 "))
    if numero_secreto != numero_adivinado :
        print("¡FALLASTE!")


print("¡ACERTASTE!")