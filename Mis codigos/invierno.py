alertas_consecutivas = 0

while True:
    temperatura = float(input("Ingrese temperatura actual: "))

    if temperatura == 0:
        print("Fin del monitoreo.")
        break


    if temperatura >= 35:
        alertas_consecutivas += 1
        print(f"Alerta {alertas_consecutivas} consecutiva")

    else:
        alertas_consecutivas = 0
        print("Temperatura normal, contador reiniciado.")

    if alertas_consecutivas == 3:
        print("\n¡¡¡ACTIVANDO ASPERSORES DE EMERGENCIA!!!")
        break