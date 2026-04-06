alertas_consecutivos = 0
while True:
    temperatura = int(input("ingrese su temperatura"))
    if temperatura >= 35:
        print("ALERTA aumento de tenperatura")
        alertas_consecutivos = alertas_consecutivos + 1
    if temperatura < 35:
        alertas_consecutivos = 0
        print("temperatura normal")

    elif alertas_consecutivos == 3:
        print("TEMPERATURA DEMASIADO ALTA")
        print("¡¡¡ACTIVANDO ASPERSORES DE EMERGENCIA!!!")
        break

    elif temperatura == 0:
        print("FIN")
        break
