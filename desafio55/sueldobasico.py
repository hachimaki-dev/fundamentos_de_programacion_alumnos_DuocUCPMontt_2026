sueldo_base = 500000
colacion = 50000
movilizacion = 30000
sueldo_liquido = 0

print(f"hola empleador tu sueldo es de{sueldo_base} se te descontara un 7% de saludo y un 10% del AFP")
descuento_salud = sueldo_base * 0.07
descuento_AFP = sueldo_base * 0.10

sueldo_liquido = colacion + movilizacion + sueldo_base - descuento_salud - descuento_AFP

print(f"tu sueldo restando la salud y afp y sumando tus bonos de volavion y movilizacion es de {sueldo_liquido}")


