# Ejercicio 52: Calculadora de Liquidación Real
# Calcula el sueldo de una persona leyendo datos desde tres lados distintos.

# Datos Iniciales: El `sueldo_base = 800000`. Sus bonos son: `{'colacion': 50000, 'movilizacion': 30000}`. Sus descuentos son `{'AFP': 0.10, 'Salud': 0.07}`.

# Reglas de Negocio: El trabajador gana la suma de su base más los bonos. Pero hay que restarle los descuentos de AFP y Salud. 
# Los descuentos se calculan multiplicando ese porcentaje SÓLO por el sueldo base (a los bonos no se les descuenta nada).

# Restricciones: Usa un `for` usando `.values()` para sumar los bonos. Usa otro `for` usando `.values()` para recorrer los porcentajes de descuento, 
# calcular la plata que significan, y restarlos. Imprime el sueldo líquido final.

sueldo_base = 800000
bonos = {'colacion': 50000, 'movilizacion': 30000}
descuentos = {'AFP': 0.10, 'Salud': 0.07}
sueldo_liquido_final = 0

for sumar_bono in bonos.values():
    sueldo_liquido_final += sumar_bono

for descuento in descuentos.values():
    sueldo_liquido_final -= sueldo_base * descuento

sueldo_liquido_final += sueldo_base
print(sueldo_liquido_final)
