sueldo_cliente = 800000
años_en_banco_cliente = 6
deudas_cliente = 0

sueldo_vip = 1000000
años_minimos = 5
deudas_permitidas = 0

if sueldo_cliente > sueldo_vip or (años_en_banco_cliente >= años_minimos and deudas_cliente == deudas_permitidas):
    print("Cliente VIP")
else:
    print("Cliente Normal")