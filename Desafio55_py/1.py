print("######"*6)
print(" Liquidación  de  Sueldo  Básico")
print("######"*6)


sueldo_base = 500000
bono_De_colacion = 50000
movilizacion = 30000
descuento = 0.17


descuento_total = sueldo_base * descuento

descuento_sueldo_base = sueldo_base - descuento_total

sueldo_base_total = descuento_sueldo_base + bono_De_colacion + movilizacion

print(sueldo_base_total)
