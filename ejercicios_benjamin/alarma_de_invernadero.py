alertas_consecutivas = 0 

while True: 
    temp = float(input("ingrese temperatura actual (o para salir): "))

    if temp == 0: 
        print("sistema detenido manualmente")
        break 
    if temp >= 35: 
        alertas_consecutivas += 1
        print("ALERTA! {alertas_consecutivas} temperatura alta") 
    else:
        alertas_consecutivas = 0
        print("temperatura normal, contador reiniciado")
        if alertas_consecutivas == 3:  print("¡¡¡¡ACTIVANDO ASPERSORES DE EMERGENCIA!!!!") 
    break
 