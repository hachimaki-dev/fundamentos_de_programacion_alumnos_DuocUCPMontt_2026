sueldo_base = 500000
bono_colacion = 50000
movilizacion = 30000
descuento_salud = 0.07
descuento_AFP = 0.1

sueldo_1 = sueldo_base * descuento_AFP 

sueldo_2 = sueldo_base * descuento_salud

sueldo_base -= sueldo_1
sueldo_base -= sueldo_2
sueldo_base += bono_colacion
sueldo_base += movilizacion


print(sueldo_base)