#Quieres calcular cuántos meses te tomará ahorrar para comprarte un auto.

#Datos Iniciales: El auto cuesta 5000000. Tú ya tienes ahorrado 1500000. Vas a ahorrar 150000 cada mes.

#Reglas de Negocio: Primero descubre cuánto dinero te falta. Luego, averigua cuántos meses completos te tomará juntar ese dinero faltante con tu ahorro mensual.

#Restricciones: Usa división entera (`//`) para asegurarte de que el resultado sea un número de meses exactos, sin decimales. Imprime solo el número de meses.
auto = 5000000
ahorrado = 1500000
cada_mes = 150000
cantidad_para_comprar_el_auto = auto - ahorrado
print(f"cantidad faltante para el auto es : {cantidad_para_comprar_el_auto}")
meses_faltante = cantidad_para_comprar_el_auto // cada_mes
print(f"la cantidad de meses faltante es: {meses_faltante}")
