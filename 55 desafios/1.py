sueldo_base = 500000
bono_colacion = 50000
bono_movilizacion = 30000

sueldo_con_descuento = sueldo_base * 0.83
sueldo_total = sueldo_con_descuento + bono_colacion + bono_movilizacion

print(f"El sueldo líquido es de ${sueldo_total}")