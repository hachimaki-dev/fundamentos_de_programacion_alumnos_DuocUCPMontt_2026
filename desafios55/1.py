##Eres el contador de la empresa y debes calcular el sueldo de un empleado.
##Datos Iniciales: El sueldo base es 500000. El bono de colación es 50000 y el de movilización es 30000.
##Reglas de Negocio: Al empleado se le descuenta un 7% por salud y un 10% por AFP. Ojo: estos descuentos se calculan SÓLO sobre el sueldo base (los bonos no sufren descuentos). El sueldo líquido es el sueldo base más los bonos, menos los descuentos.
##Restricciones: Asigna todos los valores directamente en el código (no uses inputs). Imprime sólo el número final del sueldo líquido.

sueldo_base = 500000
bono_colacion = 50000
movilizacion = 30000
descuento_salud = 0.07
descuento_AFP = 0.1

sueldo_1 = sueldo_base * descuento_AFP 

sueldo_2 = sueldo_base * descuento_salud

sueldo_base -= sueldo_1
sueldo_base -= sueldo_2
sueldo_base += bono_colacion
sueldo_base += movilizacion


print(sueldo_base)