# El cliente tiene un sueldo de 550000
#tiene 1 deuda activa
#El banco exige DOS cosas a la vez: 
# que el sueldo sea mayor a 500000 Y que la cantidad de deudas sea exactamente 0.

sueldo = 550000
deudas = 1

if sueldo > 500000 and deudas == 0:
    print("aprobado")
else:
    print("Rechazado")