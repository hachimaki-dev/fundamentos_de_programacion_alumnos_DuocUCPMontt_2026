sueldo_base = 500000
bono_colacion = 50000
bono_movilizacion = 30000

 
descuento_colacion = 7 
descuento_movilizacion = 10
# colacion + afp
descuento_total = 17

sueldo_base = 500000 - 500000  * 17 /100


sueldo_base += bono_colacion
sueldo_base += bono_movilizacion
print(sueldo_base)