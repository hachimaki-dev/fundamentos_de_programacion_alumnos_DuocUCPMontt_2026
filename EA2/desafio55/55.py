'''Ejercicio 55: Simulador de Cajero con Desglose (BancoEstado)

El Boss Final del curso: Programa el cerebro de un cajero automático para que entregue la menor cantidad de billetes posibles al dar un vuelto.

Datos Iniciales: El cliente quiere sacar 37000. Los billetes que existen son `20000, 10000, 5000 y 1000`. Crea un diccionario vacío para guardar tus resultados.

Reglas de Negocio: Para usar pocos billetes, el cajero siempre intenta pasar primero los billetes más grandes. Por ejemplo, para 37000, primero ve cuántos de 20000 caben. Con la plata que sobra, ve cuántos de 10000 caben, y así hasta llegar a cero.

Restricciones: Recorre una lista con los billetes ordenados de mayor a menor. Usa división entera (`//`) para saber cuántos billetes entregar, y guárdalo en tu diccionario como `diccionario[billete] = cantidad`. Luego, usa el módulo (`%`) para actualizar la plata que te falta por repartir. Imprime el diccionario con el desglose exacto al terminar.'''

retiro_cliente = 37000
billete_entrega = {}

billetes = [20000, 10000, 5000, 1000]
billetes.sort(reverse=True)

for billete in billetes:
    cantidad = retiro_cliente // billete
    billete_entrega[billete] = cantidad
    retiro_cliente = retiro_cliente % billete
    
print(billete_entrega)