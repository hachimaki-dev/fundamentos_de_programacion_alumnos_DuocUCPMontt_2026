# Ejercicio 55: Simulador de Cajero con Desglose (BancoEstado)
# El Boss Final del curso: Programa el cerebro de un cajero automático para que entregue la menor cantidad de billetes posibles al dar un vuelto.

# Datos Iniciales: El cliente quiere sacar 37000. Los billetes que existen son `20000, 10000, 5000 y 1000`. 
# Crea un diccionario vacío para guardar tus resultados.

# Reglas de Negocio: Para usar pocos billetes, el cajero siempre intenta pasar primero los billetes más grandes. 
# por ejemplo, para 37000, primero ve cuántos de 20000 caben. Con la plata que sobra, ve cuántos de 10000 caben, y así hasta llegar a cero.

# Restricciones: Recorre una lista con los billetes ordenados de mayor a menor. 
# Usa división entera (`//`) para saber cuántos billetes entregar, y guárdalo en tu diccionario como `diccionario[billete] = cantidad`.
# Luego, usa el módulo (`%`) para actualizar la plata que te falta por repartir. 
# Imprime el diccionario con el desglose exacto al terminar.

# Pista de Ayuda: Usa división entera // para la cantidad de billetes, y actualiza el retiro = retiro % denominacion.

monto_a_retirar = 37000
billetes_disponibles = [20000, 10000, 5000, 1000]
cantidad_por_denominacion = {}

for denominacion in billetes_disponibles:
    cantidad_por_denominacion[denominacion] = monto_a_retirar // denominacion
    monto_a_retirar = monto_a_retirar % denominacion

print(cantidad_por_denominacion)

