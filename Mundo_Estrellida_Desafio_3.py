'''
## Desafío 3: El Simulador de Cola de Banco 🏦

Un banco tiene una fila de clientes esperando ser atendidos. Cada cliente tiene un tipo de trámite que toma un tiempo diferente en minutos.

```python
Cola = [
    {'Nombre': 'Laura',   'Tramite': 'Depósito',    'Minutos': 5},
    {'Nombre': 'Roberto', 'Tramite': 'Crédito',     'Minutos': 20},
    {'Nombre': 'Sofía',   'Tramite': 'Repósito',    'Minutos': 5},
    {'Nombre': 'Marcelo', 'Tramite': 'Hipoteca',    'Minutos': 35},
    {'Nombre': 'Ignacia', 'Tramite': 'Depósito',    'Minutos': 5},
]
```

**Lo que debes lograr:**

Simula la atención uno a uno. El banco cierra cuando han pasado **45 minutos** desde que abrió. Si atender al siguiente cliente haría superar ese límite, ese cliente y todos los que siguen deben quedar en una lista llamada `sin_atender`. Al terminar, imprime a los clientes que **sí fueron atendidos** y a los que **quedaron fuera**.

**Resultado esperado en consola:**
```
Atendidos: ['Laura', 'Roberto', 'Sofía', 'Marcelo']
Sin atender: ['Ignacia']
```

**Lo que lo hace difícil:** Necesitas un acumulador de tiempo, dos listas que se van llenando según una condición, y entender que no es un filtro simple: una vez que el tiempo se agota, todos los siguientes van automáticamente a `sin_atender` sin ni siquiera revisar su tiempo.
'''

Cola = [

    {'Nombre': 'Laura',   'Tramite': 'Depósito',    'Minutos': 5},

    {'Nombre': 'Roberto', 'Tramite': 'Crédito',     'Minutos': 20},

    {'Nombre': 'Sofía',   'Tramite': 'Repósito',    'Minutos': 5},

    {'Nombre': 'Marcelo', 'Tramite': 'Hipoteca',    'Minutos': 35},

    {'Nombre': 'Ignacia', 'Tramite': 'Depósito',    'Minutos': 5},

        ]
Tiempo_Maximo_Abertura_Banco = 45

Atendidos = []

Sin_Atender = []

for Cola_Serpiente in Cola:

    print(f'Usuario: {Cola_Serpiente['Nombre']}, se tardara {Cola_Serpiente['Minutos']}')

    if Tiempo_Maximo_Abertura_Banco >= 0:

        Tiempo_Maximo_Abertura_Banco -= Cola_Serpiente['Minutos']

        Atendidos.append(Cola_Serpiente['Nombre'])

        continue

    Sin_Atender.append(Cola_Serpiente['Nombre'])


print(f"Personas atendidas: {Atendidos}")

print(f"Personas sin atender: {Sin_Atender}")