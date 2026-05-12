'''
## Desafío 2: El Resumen de Ventas 🏪

Una tienda registró todas sus ventas del día. Cada venta tiene un vendedor y un monto.

```python
ventas = [
    {'vendedor': 'Ana',    'monto': 15000},
    {'vendedor': 'Pedro',  'monto': 32000},
    {'vendedor': 'Ana',    'monto': 21000},
    {'vendedor': 'Pedro',  'monto': 8000},
    {'vendedor': 'Carlos', 'monto': 45000},
]
```

**Lo que debes lograr:**

Genera un resumen donde cada vendedor aparezca una sola vez con el total de todo lo que vendió. Al terminar, imprime el nombre del vendedor que más vendió y cuánto fue su total.

**Resultado esperado en consola:**
```
Ana: 36000
Pedro: 40000
Carlos: 45000
Ganador: Carlos con 45000
```

**Lo que lo hace difícil:** Debes construir un diccionario de totales mientras recorres la lista. Para encontrar al ganador, necesitas recorrer ese diccionario con otro `for`, rastreando el máximo con variables auxiliares, igual que hiciste en el matchmaking de ELO, pero esta vez tú decides la estructura de datos.
'''

from ast import List


Ventas = [

    {'Vendedor': 'Ana',    'Monto': 15000},

    {'Vendedor': 'Pedro',  'Monto': 32000},

    {'Vendedor': 'Ana',    'Monto': 45550},

    {'Vendedor': 'Josue',  'Monto': 8000},

    {'Vendedor': 'Pedro', 'Monto': 45000}

         ]

Ganador = None

Lista_de_Montos = []

for Datos in Ventas:

    print(f'{Datos['Vendedor']}: {Datos['Monto']}')

    Lista_de_Montos.append(Datos['Monto'])

for Victorioso in Ventas:
    if Victorioso['Monto'] == max(Lista_de_Montos):
        Ganador = Victorioso['Vendedor']
print(f'Y el ganador es: {Ganador} con {max(Lista_de_Montos)}')
