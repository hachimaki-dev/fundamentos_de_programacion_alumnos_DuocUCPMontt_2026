#Eres el contador de la empresa y debes calcular el sueldo de un empleado.
#Datos Iniciales: El sueldo base es 500000. El bono de colación es 50000 y el de movilización es 30000.
#Reglas de Negocio: Al empleado se le descuenta un 7% por salud y un 10% por AFP. Ojo: estos descuentos se calculan SÓLO sobre el sueldo base (los bonos no sufren descuentos). El sueldo líquido es el sueldo base más los bonos, menos los descuentos.
#Restricciones: Asigna todos los valores directamente en el código (no uses inputs). Imprime sólo el número final del sueldo líquido.
#Resultado esperado en consola:

sueldo = 500000
bono = 50000
movilizacion = 30000
descuento_salud = 0.07
descuento_afp = 0.10
descuento_salud = sueldo * 0.07
descuento_afp = sueldo * 0.10
sueldo_liquido = sueldo + bono + movilizacion - (descuento_afp + descuento_salud) 
print(f"el sueldo liquido es:{sueldo_liquido}")


