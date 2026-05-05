#CALCULAR EL SUELDO DE UN EMPLEDO

sueldo_base = 500000 
bono_colacion = 50000 
bono_movilización = 30000

descuento_salud = sueldo_base * 0.07
descuento_afp = sueldo_base * 0.10
sueldo_liquido = sueldo_base - descuento_salud - descuento_afp + bono_colacion + bono_movilización
print(sueldo_liquido)
