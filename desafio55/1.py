sueldo = 500000
bono_colacion = 50000 
bono_de_movilizacion = 30000



descuento_por_salud =  sueldo*7/100
descuento_por_afp = sueldo*10/100
nuevo_sueldo = sueldo - (descuento_por_afp + descuento_por_salud)
total = nuevo_sueldo + (bono_colacion + bono_de_movilizacion)
print(total)