sueldo_base = 800000
bonos = {'colacion': 50000, 'movilizacion': 30000}
descuentos_pct = {'AFP': 0.10, 'Salud': 0.07}

total_ingresos = sueldo_base
for monto_bono in bonos.values():
    total_ingresos += monto_bono


sueldo_liquido = total_ingresos
for porcentaje in descuentos_pct.values():
    descuento_dinero = sueldo_base * porcentaje
    sueldo_liquido -= descuento_dinero

print(f"El sueldo líquido final es: ${int(sueldo_liquido)}")
