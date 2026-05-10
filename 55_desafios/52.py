#Calcula el sueldo de una persona leyendo datos desde tres lados distintos.
sueldo_base = 800000
bonos = {'colacion': 50000, 'movilizacion': 30000}
descuentos = {'AFP': 0.10, 'Salud': 0.07}

#Reglas de Negocio: El trabajador gana la suma de su base más los bonos. Pero hay que restarle los descuentos de AFP y Salud. Los descuentos se calculan multiplicando ese porcentaje SÓLO por el sueldo base (a los bonos no se les descuenta nada).

#Restricciones: Usa un `for` usando `.values()` para sumar los bonos. Usa otro `for` usando `.values()` para recorrer los porcentajes de descuento, calcular la plata que significan, y restarlos. Imprime el sueldo líquido final.

descuento_total = 0
bono_total = 0

for i in bonos.values():
    bono_total += i

for i in descuentos.values():
    descuento_total += sueldo_base * i

sueldo_final = sueldo_base + bono_total - descuento_total
print(sueldo_final)