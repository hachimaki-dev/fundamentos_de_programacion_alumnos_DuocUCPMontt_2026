sueldo_base = 500000
bono_colacion = 50000
bono_movilizacion = 30000

descuento_salud = sueldo_base // 7
descuento_afp = sueldo_base // 10

sueldo_descontado = ((sueldo_base - descuento_afp) - descuento_salud)
sueldo_liquido = (sueldo_descontado + bono_colacion) + bono_movilizacion
print(f"Su sueldo es de {sueldo_liquido}")