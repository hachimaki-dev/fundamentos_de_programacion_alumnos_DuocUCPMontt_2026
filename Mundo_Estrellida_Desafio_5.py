'''
## Desafío 5: El Analizador de Partidas 🕹️

Al terminar una sesión de juego, el sistema registra si cada partida fue ganada o perdida, y el tiempo que duró en minutos.

```python
partidas = [
    {'resultado': 'victoria', 'minutos': 32},
    {'resultado': 'derrota',  'minutos': 18},
    {'resultado': 'victoria', 'minutos': 45},
    {'resultado': 'derrota',  'minutos': 22},
    {'resultado': 'victoria', 'minutos': 38},
    {'resultado': 'derrota',  'minutos': 11},
]
```

**Lo que debes lograr:**

Con un solo `for` que recorra la lista una única vez, calcula todo lo siguiente:

1. Total de victorias y total de derrotas.
2. Tiempo total jugado (todas las partidas sumadas).
3. Duración promedio **solo de las victorias** (suma de minutos de victorias ÷ número de victorias).

Imprime los cuatro valores al final.

**Resultado esperado en consola:**
```
Victorias: 3
Derrotas: 3
Tiempo total: 166 minutos
Promedio victorias: 38.33 minutos
```

**Lo que lo hace difícil:** Todo debe salir de un único recorrido. 

Necesitas mantener al menos cinco variables acumuladoras en paralelo, 
actualizar las correctas en cada iteración según la condición, 
y calcular el promedio recién al final, fuera del ciclo. 

Si lo haces con varios `for`, estás repitiendo trabajo: el desafío es resolverlo todo de una pasada.'''


Partidas = [

    {'Resultado': 'Victoria', 'Minutos': 32},

    {'Resultado': 'Derrota',  'Minutos': 18},

    {'Resultado': 'Victoria', 'Minutos': 45},

    {'Resultado': 'Derrota',  'Minutos': 22},

    {'Resultado': 'Victoria', 'Minutos': 38},

    {'Resultado': 'Derrota',  'Minutos': 11},
            
            ]

Score = {

    'Victorias' : 0,

    'Derrotas' : 0,

    'Tiempo_de_Victorias' : 0,

    'Tiempo_de_Derrotas' : 0

         }

for X in range(len(Partidas)):

    if Partidas[X]['Resultado'] == 'Victoria':

        Score['Victorias'] += 1

        Score['Tiempo_de_Victorias'] += Partidas[X]['Minutos']

    elif Partidas[X]['Resultado'] == 'Derrota':

        Score['Derrotas'] += 1

        Score['Tiempo_de_Derrotas'] += Partidas[X]['Minutos']


print(f'''
      
Victorias: {Score['Victorias']}

Derrotas: {Score['Derrotas']}

Tiempo total: {Score['Tiempo_de_Victorias'] + Score['Tiempo_de_Derrotas']} Minutos

Promedio de las Victorias: {Score['Tiempo_de_Victorias']/Score['Victorias']} Minutos

''')