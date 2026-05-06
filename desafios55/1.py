sueldo_base = 500000
bono_movilizacion = 30000
bono_colacion = 50000

descuento_afp = sueldo_base * 0.10
descuento_salud = sueldo_base * 0.07

sueldo_empleado_descuento = sueldo_base - descuento_afp - descuento_salud

sueldo_empleado_total = sueldo_empleado_descuento + bono_colacion + bono_movilizacion

print (sueldo_empleado_total)

#a