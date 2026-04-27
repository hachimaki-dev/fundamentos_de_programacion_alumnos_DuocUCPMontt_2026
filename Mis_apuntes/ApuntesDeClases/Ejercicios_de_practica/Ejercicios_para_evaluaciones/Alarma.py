alertas_consecutivas = 0

while True:
    temperatura_actual = float(input("Cual es la temperatura actual? "))
    if temperatura_actual == 0:
        break
    if temperatura_actual >= 35:
        alertas_consecutivas += 1
        print(f"Llevas {alertas_consecutivas} alertas.")
    elif temperatura_actual < 35:
        alertas_consecutivas = 0
        print(f"Llevas {alertas_consecutivas} alertas.")
    if alertas_consecutivas == 3:
        print("¡¡¡¡¡¡ACTIVANDO ASPERSORES DE EMERGENCIA!!!!!")
        break