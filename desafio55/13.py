sueldo_cliente = 800000
tiempo_siendo_cliente = 6 # años
deudas_cliente = 0

if sueldo_cliente > 1000000 or (tiempo_siendo_cliente >= 5 and deudas_cliente == 0):
    print("Cliente VIP")
else:
    print("Cliente normal")
