monto_a_retirar = 37000
billetes_disponibles = [20000, 10000, 5000, 1000]
resultado_desglose = {}
for billete in billetes_disponibles:
    cantidad = monto_a_retirar // billete
    if cantidad > 0:
        resultado_desglose[billete] = cantidad
        monto_a_retirar = monto_a_retirar % billete
print(resultado_desglose)