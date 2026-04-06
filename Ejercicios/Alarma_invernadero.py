contador_alertas_consecutivas = 0
while True:
    t_actual = int(input("Ingrese la temperatura actual del invernadero: "))
    if t_actual >= 35:
        contador_alertas_consecutivas = contador_alertas_consecutivas + 1
        if contador_alertas_consecutivas == 3:
            print("¡¡¡ACTIVANDO ASPERSORES DE EMERGENCIA!!!")
            break
    elif t_actual == 0:
        break
    elif t_actual < 35:
        contador_alertas_consecutivas = 0
    
