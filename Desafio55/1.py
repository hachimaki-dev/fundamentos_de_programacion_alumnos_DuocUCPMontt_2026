sueldo_base=500000
bono_colacion=50000
movilizacion=30000
descuento_salud= sueldo_base*0.07
descuento_afp= sueldo_base*0.1
sueldo_base=(sueldo_base-descuento_afp)-descuento_salud
sueldo_liquido=sueldo_base+bono_colacion+movilizacion
print(sueldo_liquido)