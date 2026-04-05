alertas_consecutivas = 0

while True:
    temperatura = float(input("Registre la temperatura de hoy: "))

    if temperatura == 0:
        print("Fin del monitoreo. ")
        break

    if temperatura >= 35:
        alertas_consecutivas +=1
        print("Alerta:", alertas_consecutivas, "temperaturas subiendo!!")

    else:
        alertas_consecutivas = 0
        print("Temperatura normal, contador reiniciado")
    
    if alertas_consecutivas == 3:
        print(" SE QUEMA EL MUNDOOOO, ACTIVANDO ASPERSORES DE EMERGENCIA!!!!")

    break