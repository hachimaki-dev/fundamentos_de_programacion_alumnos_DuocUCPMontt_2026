#Quieres calcular cuántos meses te tomará ahorrar para comprarte un auto.
#Datos Iniciales: El auto cuesta 5000000. Tú ya tienes ahorrado 1500000. Vas a ahorrar 150000 cada mes.
#Reglas de Negocio: Primero descubre cuánto dinero te falta. Luego, averigua cuántos meses completos te tomará juntar ese dinero faltante con tu ahorro mensual.
#Restricciones: Usa división entera (`//`) para asegurarte de que el resultado sea un número de meses exactos, sin decimales. Imprime solo el número de meses.
costo_auto = 5000000
monto_ahorrado = 1500000
monto_a_ahorrar_por_mes = 150000
dinero_faltante = costo_auto - monto_ahorrado
meses_faltantes = dinero_faltante // monto_a_ahorrar_por_mes
print(meses_faltantes)