sueldo_neto = 500000
bonoC = 50000
bonoM = 30000
descuento_afp = .10 * sueldo_neto
descuento_salud = .07 * sueldo_neto
sueldo_liquido = sueldo_neto - (descuento_afp + descuento_salud)
print(f"{sueldo_liquido + bonoC + bonoM}")