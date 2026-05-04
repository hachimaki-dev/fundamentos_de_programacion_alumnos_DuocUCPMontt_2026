sueldo_cliente = 550000
deuda = 1
print(f"CONDICIONES, TENER UN SUELDO MAYOR A $500000CLP Y NO TENER NINGUNA DEUDA")

if sueldo_cliente > 500000 and deuda == 0:
    print("APROBADO")
else:
    print("RECHAZADO")