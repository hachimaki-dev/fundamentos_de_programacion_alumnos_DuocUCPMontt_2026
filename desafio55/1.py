sueldo_base = 500000
bono_colacion = 50000
bono_movilizacion = 30000
descuento = 0.17


descuento = sueldo_base * descuento


sueldo_base = sueldo_base - descuento


sueldo_base = sueldo_base + bono_colacion + bono_movilizacion 


print(sueldo_base)