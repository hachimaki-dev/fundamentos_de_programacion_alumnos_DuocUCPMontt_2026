sueldo_base = 500000
colacion = 50000
movilizacion = 30000

afp = sueldo_base * 0.1
salud = sueldo_base * 0.07
descuento = afp + salud
bonos_total = colacion + movilizacion

sueldo_liquido = (sueldo_base + bonos_total) - descuento
print(f"Sueldo líquido: ${sueldo_liquido}")