sueldo_base= 500000

bono_colacion = 50000

movilizacion = 30000


descuento_empleado = sueldo_base * 0.07

descuento_afp = sueldo_base * 0.10

sueldo_liquido = sueldo_base + bono_colacion + movilizacion - descuento_empleado - descuento_afp 

print(f"tu sueldo es: {int(sueldo_liquido)}")

