#Ejercicio 13: Promoción VIP BancoEstado (OR y AND)

sueldo_cliente =  800000
deudas = 0
años = 6
if (sueldo_cliente > 100000) or (años > 5 and deudas == 0):
    print("Cliente VIP")
else:
    print("Cliente normal")