''''Ejercicio 46: Suma de Ventas (Cornershop)
Suma todas las ganancias de los locales sin importar cómo se llamen.

Datos Iniciales: Las ventas son: `{'LocalA': 150, 'LocalB': 300, 'LocalC': 100}`.

Reglas de Negocio: A la gerencia no le importa qué local vendió qué cosa, solo quieren saber cuánta plata se hizo en total.

Restricciones: No uses la función rápida `sum()`. 

Extrae solamente los números usando la herramienta `.values()` y súmalos uno por uno adentro de un ciclo `for`. Imprime el total.'''

Total = 0

Ventas_Por_Local = {

                    'LocalA': 150, 

                    'LocalB': 300, 

                    'LocalC': 100

                    }

for Ventas in Ventas_Por_Local.values():
    Total += Ventas

print(Total)