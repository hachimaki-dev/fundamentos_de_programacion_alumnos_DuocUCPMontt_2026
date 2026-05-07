#Calcula el sueldo de una persona leyendo datos desde tres lados distintos.

#Datos Iniciales: El `sueldo_base = 800000`. Sus bonos son: `{'colacion': 50000, 'movilizacion': 30000}`. Sus descuentos son `{'AFP': 0.10, 'Salud': 0.07}`.

#Reglas de Negocio: El trabajador gana la suma de su base más los bonos. Pero hay que restarle los descuentos de AFP y Salud. Los descuentos se calculan multiplicando ese porcentaje SÓLO por el sueldo base (a los bonos no se les descuenta nada).

#Restricciones: Usa un `for` usando `.values()` para sumar los bonos. Usa otro `for` usando `.values()` para recorrer los porcentajes de descuento, calcular la plata que significan, y restarlos. Imprime el sueldo líquido final.

sueldo_base = 800000
bonos = {"colacion": 50000, "movilizacion": 30000}
descuentos = {"afp": 0.10, "salud" : 0.07}
total_bonos = 0
for bono in bonos.values():
    total_bonos += bono 
    sueldo_con_bonos = sueldo_base + total_bonos
    total_descuentos = 0
    for descuento in descuentos.values():
        total_descuentos += sueldo_base * descuento

        