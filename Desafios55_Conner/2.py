#Ejercicio 2: Proyección de Ahorro para un Auto
#Quieres calcular cuántos meses te tomará ahorrar para comprarte un auto.

#Datos Iniciales: El auto cuesta 5.000.000. Tú ya tienes ahorrado 1.500.000. Vas a ahorrar 150.000 cada mes.

#Reglas de Negocio: Primero descubre cuánto dinero te falta. Luego,averigua cuántos meses completos te tomará juntar ese dinero faltante con tu ahorro mensual.

#Restricciones: Usa división entera (`//`) para asegurarte de que el resultado sea un número de meses exactos, sin decimales. 
#Imprime solo el número de meses.

valor_auto=5000000
ahorros=1500000
ahorros_mensuales=150000

diferencia=valor_auto-ahorros #3.500.000
meses=diferencia//ahorros_mensuales

print(meses)