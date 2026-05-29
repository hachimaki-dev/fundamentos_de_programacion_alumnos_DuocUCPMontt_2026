sueldo_cliente = 550000
deudas_activas = 1
minimo_credito = 500000
if sueldo_cliente > minimo_credito and deudas_activas == 0:
    print("Credito aprobado")
else:
    print("Crédito Rechazado")