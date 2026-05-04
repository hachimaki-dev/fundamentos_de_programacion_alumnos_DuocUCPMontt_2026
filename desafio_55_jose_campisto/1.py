sueldo_base=500000
bono_colacion=50000
movilizacion=30000

descuento_salud=sueldo_base*0.07
print(descuento_salud)
afp=sueldo_base*0.1

sueldo_base-= descuento_salud + afp
sueldo_base+= movilizacion + bono_colacion


print(sueldo_base)
