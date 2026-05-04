#Ejercicio 1: Liquidación de Sueldo Básico
#Eres el contador de la empresa y debes calcular el sueldo de un empleado.

#Datos Iniciales: El sueldo base es 500000. El bono de colación es 50000 y el de movilización es 30000.

#Reglas de Negocio: Al empleado se le descuenta un 7% por salud y un 10% por AFP. Ojo: estos descuentos se calculan SÓLO sobre el sueldo base (los bonos no sufren descuentos). El sueldo líquido es el sueldo base más los bonos, menos los descuentos.

#Restricciones: Asigna todos los valores directamente en el código (no uses inputs). #Imprime sólo el número final del sueldo líquido.
sueldo_descuento = 0
sueldo_base= 500000
bono_colacion = 50000
movilizacion = 30000
sueldo_liquido = 0 
print("--calculadora--")
print(f"Hola , este es su sueldo base : {sueldo_base} , este es su bono de colacion : {bono_colacion} y este es su bono de movilizacion : {movilizacion} ")
sueldo_descuento = (sueldo_base - 85000) 
sueldo_liquido = sueldo_descuento + bono_colacion + movilizacion
print(f"ahora su sueldo liquido es : {sueldo_liquido}")