num_secreto = 5
num_escogido = 0

while num_escogido != num_secreto:
    num_escogido = int(input("Ingrese un número del 1 al 10: "))
    if num_escogido != num_secreto and num_escogido != 0:
        print("Te equivocaste lero lero")

print("¡Ganaste yay!")