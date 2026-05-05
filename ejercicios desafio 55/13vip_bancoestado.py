sueldo_cliente = 800000
años_antiguedad = 6
deudas = 0
opcion_vip1 = sueldo_cliente > 1000000
opcion_vip2 = años_antiguedad >= 5 and deudas == 0
if opcion_vip1 or opcion_vip2 == True:
    print("cliente VIP")
else: 
    print("cliente regular")