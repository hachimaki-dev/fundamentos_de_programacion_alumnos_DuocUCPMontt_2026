###Ejercicio 2: Proyección de Ahorro para un Auto
### Quieres calcular cuántos meses te tomará ahorrar para comprarte un auto.
###Datos Iniciales: El auto cuesta 5000000. Tú ya tienes ahorrado 1500000. Vas a ahorrar 150000 cada mes.
###Reglas de Negocio: Primero descubre cuánto dinero te falta. Luego, averigua cuántos meses completos te tomará juntar ese dinero faltante con tu ahorro mensual.
###Restricciones: Usa división entera (`//`) para asegurarte de que el resultado sea un número de meses exactos, sin decimales. Imprime solo el número de meses.

precio_auto = 5000000
ahorro_actual = 1500000
ahorro_mensual = 150000

print((precio_auto - ahorro_actual) // ahorro_mensual)
