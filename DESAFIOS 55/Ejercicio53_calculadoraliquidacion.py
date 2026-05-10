sueldo_base = 800000
bonos= {'colacion': 50000, 'movilizacion': 30000} 
descuentos={'AFP': 0.10, 'Salud': 0.07}
totalbonos=0
totaldescuentos=0
for i in bonos.values():
    totalbonos+=i
for i in descuentos.values():
    totaldescuentos+=(sueldo_base*i)
liquidacion=sueldo_base+totalbonos-totaldescuentos
print(liquidacion)
#Reglas de Negocio: El trabajador gana la suma de su base más los bonos. Pero hay que restarle los descuentos de AFP y Salud. Los descuentos se calculan multiplicando ese porcentaje SÓLO por el sueldo base (a los bonos no se les descuenta nada).

#Restricciones: Usa un `for` usando `.values()` para sumar los bonos. Usa otro `for` usando `.values()` para recorrer los porcentajes de descuento, calcular la plata que significan, y restarlos. Imprime el sueldo líquido final.