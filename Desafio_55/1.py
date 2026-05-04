sueldo_base = 500000
bono_colacion = 50000
bono_moviizacion = 30000

sueldo_base_D1 = sueldo_base * 0.07
print(f"7% de descuento en sueldo base: ${sueldo_base_D1}")
sueldo_base_D2 = sueldo_base * 0.1
print(f"10% de descuento en sueldo base: ${sueldo_base_D2}")

sueldo_final = sueldo_base - sueldo_base_D1 - sueldo_base_D2
print(f"Sueldo final, es el sueldo base con los descuentos: ${sueldo_final}")
sueldo_liquido = sueldo_final + bono_colacion + bono_moviizacion

print(f"Este es el sueldo liquido, con los bonos y los descuentos: ${sueldo_liquido}")




