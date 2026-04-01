alerta_consecutiva = 0
while True:
    temperatura_actual = float(input("Ingrese temperatura actual: "))
    if temperatura_actual == 0:
        print("Sistema detenido")
        break
    if temperatura_actual >= 35:
        alerta_consecutiva += 1
        print(f"Alerta consecutiva {alerta_consecutiva}")
    else:
        alerta_consecutiva = 0
        print("Temperatura normal")
    if alerta_consecutiva == 3:
        print("¡¡¡ACTIVANDO ASPERSORES DE EMERGENCIA!!!")
        break