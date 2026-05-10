#El Boss Final del curso: Programa el cerebro de un cajero automático para que entregue la menor cantidad de billetes posibles al dar un vuelto.

cliente = 37000
billetes = [20000, 10000, 5000 , 1000]

#Reglas de Negocio: Para usar pocos billetes, el cajero siempre intenta pasar primero los billetes más grandes. Por ejemplo, para 37000, primero ve cuántos de 20000 caben. Con la plata que sobra, ve cuántos de 10000 caben, y así hasta llegar a cero.

#Restricciones: Recorre una lista con los billetes ordenados de mayor a menor. Usa división entera (`//`) para saber cuántos billetes entregar, y guárdalo en tu diccionario como `diccionario[billete] = cantidad`. Luego, usa el módulo (`%`) para actualizar la plata que te falta por repartir. Imprime el diccionario con el desglose exacto al terminar.

resultado = {}

for i in billetes:
    cantidad = cliente // i
    resultado[i] = cantidad
    cliente = cliente % i

print(resultado)