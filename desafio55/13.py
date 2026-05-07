sueldo_cliente = 800000
deudas_cliente = 0
annos = 6
if sueldo_cliente > 1000000 or (deudas_cliente == 0 and annos >= 5):
    print("Cliente VIP")
else:
    print("Cliente Normal")