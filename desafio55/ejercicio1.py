sueldo_base = 500000
bono_colacion = 50000
bono_movilizacion = 30000

descuento_salud = (sueldo_base * 0.07) 
descuento_afp = (sueldo_base * 0.1) 

sueldo_base_descuentos = sueldo_base - descuento_salud - descuento_afp
sueldo_final = sueldo_base_descuentos + bono_colacion + bono_movilizacion

print(sueldo_final)


