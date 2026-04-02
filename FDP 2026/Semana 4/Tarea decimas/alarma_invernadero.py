alertas_consecutivas = 0

while True:
    temp_actual = int(input("Ingrese la temperatura actual: "))

    if temp_actual == 0:
        break

    if temp_actual >= 35:
        alertas_consecutivas += 1
    else:
        alertas_consecutivas = 0

    if alertas_consecutivas == 3:
        print("¡¡¡ACTIVANDO ASPERSORES DE EMERGENCIA!!")
        break