print("bienvenido")
alerta_consecutiva = 0
while True :
    temperatura = int(input("ingrese temperatura actual"))
    if temperatura == 0 :
        print("FIN")
        break
    elif temperatura >= 35 :
        print("peligro mucha temperatura")
        alerta_consecutiva = alerta_consecutiva + 1
    elif temperatura < 35 :
        print("temperatura normal")
        alerta_consecutiva = 0
    if alerta_consecutiva == 3 :
        print("PELIGRO")
        print("¡¡¡ACTIVANDO ASPERSORES DE EMERGENCIA!!!")
        break