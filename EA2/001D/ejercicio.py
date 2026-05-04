sueldo_base = 500000
bono_colacion = 50000
bono_movilizacion = 30000
valor_descuento_afp_salud = sueldo_base * (17/100)
sueldo_base_con_descuento = sueldo_base - valor_descuento_afp_salud
sueldo_liquido = sueldo_base_con_descuento +bono_colacion +bono_movilizacion
print(sueldo_liquido) 