limite_de_peligro = 35
alertas_consecutivas = 0

while True:
    temperatura_actual = int(input("Ingrese temperatura actual en grados Celsisus: "))
    if temperatura_actual == 0:
        break
    elif temperatura_actual >= 35:
        alertas_consecutivas += 1
        print("¡Alerta! Temperatura peligrosa.")
        print(f"Alertas acumuladas: {alertas_consecutivas}")
    else:
        alertas_consecutivas = 0

    if alertas_consecutivas >= 3:
        print("¡¡¡ACTIVANDO ASPERSORES DE EMERGENCIA!!!")
        break
    else:
        continue
