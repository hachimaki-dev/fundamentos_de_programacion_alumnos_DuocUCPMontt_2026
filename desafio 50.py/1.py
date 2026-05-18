sueldo_base= 500000
bono_de_colacion = 50000
bono_de_movilizacion = 30000
afp=0.10
sueldo_liquido=0
salud= 0.07
descuento_salud = sueldo_base * salud
descuento_afp = sueldo_base * afp
sueldo_liquido= sueldo_base - descuento_salud - descuento_afp
print(sueldo_liquido)






