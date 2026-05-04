sueldo_base = 500000
bono_de_colacion = 50000
bono_movilizacion = 30000
descuentos = (sueldo_base * 17) /100
sueldo_base_descuento = sueldo_base - descuentos
sueldo_liquido = sueldo_base_descuento + bono_de_colacion + bono_movilizacion
print(sueldo_liquido)
