'''Ejercicio 52: Calculadora de Liquidación Real
Calcula el sueldo de una persona leyendo datos desde tres lados distintos.

Datos Iniciales: El `sueldo_base = 800000`. Sus bonos son: `{'colacion': 50000, 'movilizacion': 30000}`. Sus descuentos son `{'AFP': 0.10, 'Salud': 0.07}`.

Reglas de Negocio: El trabajador gana la suma de su base más los bonos. 

Pero hay que restarle los descuentos de AFP y Salud. Los descuentos se calculan multiplicando ese porcentaje SÓLO por el sueldo base (a los bonos no se les descuenta nada).

Restricciones: Usa un `for` usando `.values()` para sumar los bonos. Usa otro `for` usando `.values()` para recorrer los porcentajes de descuento, 
calcular la plata que significan, y restarlos. Imprime el sueldo líquido final.'''

Sueldo_Base = 800000

Bonos = {'Colacion': 50000, 'Movilizacion': 30000}

Descuentos = {'AFP': 0.10, 'Salud': 0.07}

Total = 0

Suma_Bonos = (Bonos['Colacion'] + Bonos['Movilizacion'])


Total = Sueldo_Base - (Sueldo_Base * Descuentos['AFP']) - (Sueldo_Base * Descuentos['Salud']) + Suma_Bonos

print(Total)