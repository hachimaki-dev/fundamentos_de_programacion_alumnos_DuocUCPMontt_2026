Sueldo_base = 500000
Bono_colacion = 50000
movilizacion = 30000
descuento_afp = 35000
descuento_salud = 50000

Sueldo_base = Sueldo_base - descuento_afp - descuento_salud
Sueldo_base = Sueldo_base + Bono_colacion + movilizacion

print(Sueldo_base)
