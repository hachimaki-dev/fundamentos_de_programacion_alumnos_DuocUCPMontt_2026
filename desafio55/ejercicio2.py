#Quieres calcular cuántos meses te tomará ahorrar para comprarte un auto.
#Datos Iniciales: El auto cuesta 5000000. Tú ya tienes ahorrado 1500000. Vas a ahorrar 150000 cada mes.
#Reglas de Negocio: Primero descubre cuánto dinero te falta. Luego, averigua cuántos meses completos te tomará juntar ese dinero faltante con tu ahorro mensual.
#Restricciones: Usa división entera (`//`) para asegurarte de que el resultado sea un número de meses exactos, sin decimales. Imprime solo el número de meses.

civic = 5000000
ahorrado = 1500000
ahorrado_mensual = 150000
faltante = civic - ahorrado
meses = faltante // ahorrado_mensual
print(f"los meses que faltan para tu honda civic son: {meses} meses :)")