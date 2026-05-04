#Quieres calcular cuántos meses te tomará ahorrar para comprarte un auto.

#Datos Iniciales: El auto cuesta 5000000. Tú ya tienes ahorrado 1500000. Vas a ahorrar 150000 cada mes.

#Reglas de Negocio: Primero descubre cuánto dinero te falta. Luego, averigua cuántos meses completos te tomará juntar ese dinero faltante con tu ahorro mensual.

#Restricciones: Usa división entera (`//`) para asegurarte de que el resultado sea un número de meses exactos, sin decimales. Imprime solo el número de meses.

valor_auto = 5000000
dinero_ahorrado = 1500000
ahorro_mensual = 150000

cuanto_falta = (valor_auto - dinero_ahorrado)

meses_faltantes = (ahorro_mensual * 23)

print(f"El auto a comprar cuesta {valor_auto}.")

input()

print("Sin embargo solo tengo 1500000 ahorrados.")

input()

print(f"Entonces me faltarian {cuanto_falta} para comprar el auto.")

input()

print(f"Si ahorro {ahorro_mensual} todos los meses tendria que ahorrar 23 meses para lograr este monto : {meses_faltantes}. con un margen de solo 50.000$.")
