# Liquidación de Sueldo Básico

sueldo_base = 500000
bono_de_colacion = 50000
movilizacion = 30000
#Salud y AFP
calculo1 = sueldo_base * 0.83
sueldo_final = calculo1 + bono_de_colacion + movilizacion
print(sueldo_final)