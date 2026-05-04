sueldo_base = 500000
bono_colacion = 50000
bono_movilización = 30000

descuento_1 = sueldo_base * 0.07

descuento_2 = sueldo_base * 0.1

descuento_total = descuento_1 + descuento_2

print(f"el Sueldo liquido es de ${sueldo_base + bono_colacion + bono_movilización - descuento_total}")


