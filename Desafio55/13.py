sueldo = 800000
anos_cliente = 6
deuda_activa = 0

if sueldo > 1000000 or (anos_cliente >= 5 and deuda_activa == 0):
    print("Cliente VIP")
else:
    print("Cliente normal")