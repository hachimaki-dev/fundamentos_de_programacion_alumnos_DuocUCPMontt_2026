
#Crear un algoritmo que obligue al usuario a adivinar un numero secreto previamente determinado por el sistema (del 1 al 10)
#si falla, indicarle que fallo y solicitarla que vuelva a intenarlo, si acierta, lo felicitamos y termina el programa

numero_secreto = 8
numero_ingresado = 0

while numero_secreto != numero_ingresado :
    numero_ingresado = int(input("Escoja un numero entre 1 y 10: "))
    if numero_secreto != numero_ingresado :
        print("Fallaste")

print("Correcto")




