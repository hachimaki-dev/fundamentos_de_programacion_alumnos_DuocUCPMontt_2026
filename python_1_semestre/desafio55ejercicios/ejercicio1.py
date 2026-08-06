""" Ejercicio 1: Liquidación de Sueldo Básico
Eres el contador de la empresa y debes calcular el sueldo de un empleado.

Datos Iniciales: El sueldo base es 500000. El bono de colación es 50000 
y el de movilización es 30000.

Reglas de Negocio: Al empleado se le descuenta un 7% por salud y un 10% por AFP.
 Ojo: estos descuentos se calculan SÓLO sobre el sueldo base 
 (los bonos no sufren descuentos). El sueldo líquido es el sueldo base más 
 los bonos,menos los descuentos.

Restricciones: Asigna todos los valores directamente en el código (no uses inputs). 
Imprime sólo el número final del sueldo líquido."""

sueldo_base = 500000
colacion = 50000
movilizacion = 30000

sueldo_base = sueldo_base - (sueldo_base * 0.07)# descuento de salud 
sueldo_base = sueldo_base - (sueldo_base * 0.10)# descuento de afp
sueldo_base = sueldo_base + colacion + movilizacion 

print(f"tu sueldo es: {sueldo_base}")
