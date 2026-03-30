num_inicio = 0
num_final = -1

multiplo = 0

print("Te voy a decir que número son múltiplos de un número que me des, en un rango que me des")

while multiplo < 1:
    multiplo = int(input("Ingrese el número que quiere saber sus múltiplos"))

    if multiplo < 1:
        print("El número ingresado debe ser mayor a 0")

while(num_inicio > num_final):
    num_inicio = int(input("Ingrese el número con el cual comenzar: "))
    num_final = int(input("Ingrese el número con el cual terminar: "))

    if num_inicio >= num_final:
        print("El número inicial debe ser menor al final")


