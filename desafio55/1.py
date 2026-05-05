sueldo_base = 500000
bono_colacion = 50000
bono_movilizacion = 30000

porsentaje_descuento_afp = 10
porsentaje_descuento_salud = 7 

descuento_afp =  ( sueldo_base * porsentaje_descuento_afp ) / 100
descuento_afp =  ( sueldo_base * porsentaje_descuento_salud ) / 100

liquido = sueldo_base  + bono_colacion  - bono_movilizacion - descuento_afp
print(liquido)