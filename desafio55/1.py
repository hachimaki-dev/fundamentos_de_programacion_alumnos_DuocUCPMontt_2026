"""
Ejercicio 1: Liquidación de Sueldo Básico
Eres el contador de la empresa y debes calcular el sueldo de un empleado.

Datos Iniciales: El sueldo base es 500000. El bono de colación es 50000 y el de movilización es 30000.

Reglas de Negocio: Al empleado se le descuenta un 7% por salud y un 10% por AFP. Ojo: estos descuentos se calculan SÓLO sobre el sueldo base 
(los bonos no sufren descuentos). El sueldo líquido es el sueldo base más los bonos, menos los descuentos.

Restricciones: Asigna todos los valores directamente en el código (no uses inputs). Imprime sólo el número final del sueldo líquido.

Resultado esperado en consola:
495000.0
"""

sueldo_base = 500000
bono_colacion = 50000
bono_movilización = 30000

descuento_salud = 0.07
descuento_afp = 0.1 

descuento_salud = sueldo_base * descuento_salud
descuento_afp = sueldo_base * descuento_afp

sueldo_liquido = sueldo_base + bono_colacion + bono_movilización - descuento_salud - descuento_afp

print(f"El sueldo a pagar es: {sueldo_liquido}")
