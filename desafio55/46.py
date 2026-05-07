#Suma todas las ganancias de los locales sin importar cómo se llamen.
#Datos Iniciales: Las ventas son: `{'LocalA': 150, 'LocalB': 300, 'LocalC': 100}`.
#Reglas de Negocio: A la gerencia no le importa qué local vendió qué cosa, solo quieren saber cuánta plata se hizo en total.
#Restricciones: No uses la función rápida `sum()`. 
#Extrae solamente los números usando la herramienta `.values()` y súmalos uno por uno adentro de un ciclo `for`. Imprime el total.
ventas = {"LocalA": 150, "LocalB": 300, "LocalC": 100}
total_ganancias = 0 
for ganancia in ventas.values():
    total_ganancias += ganancia

print(total_ganancias)