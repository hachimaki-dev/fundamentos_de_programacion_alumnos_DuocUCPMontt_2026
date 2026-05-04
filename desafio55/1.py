sueldo_base = 500000
bono_colacion = 50000
movilizacion = 30000
salud = 7
afp = 10

descuento_afp = (sueldo_base * salud)/100
descuento_salud = (sueldo_base * afp)/100
sueldo_liquido = sueldo_base - descuento_afp - descuento_salud + bono_colacion + movilizacion

print(f"Tu sueldo liquido es de: {sueldo_liquido}")   