#Quieres calcular cuántos meses te tomará ahorrar para comprarte un auto.

#Datos Iniciales: El auto cuesta 5000000. Tú ya tienes ahorrado 1500000. Vas a ahorrar 150000 cada mes.

#Reglas de Negocio: Primero descubre cuánto dinero te falta. Luego, averigua cuántos meses completos te tomará juntar ese dinero faltante con tu ahorro mensual.

#Restricciones: Usa división entera (`//`) para asegurarte de que el resultado sea un número de meses exactos, sin decimales. Imprime solo el número de meses.
falta_ahorrar = 0 
auto = 5000000 
alcancia =  1500000
ahorro = 150000
print(f"El valor del auto es {auto} , usted ya tiene ahorrado {alcancia} y cada mes usted ahorra {ahorro}")
falta_ahorrar = alcancia - auto
print(f"falta ahorrar = {falta_ahorrar}")
falta_ahorrar = falta_ahorrar // 24
print(f"Usted debe ahorrar en 24 meses la cantidad de {falta_ahorrar}")