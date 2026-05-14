'''
## Desafío 7: El Simulador de Ligas 🏟️

Este es el más complejo del set. Tienes los resultados de todos los partidos de una liga de fútbol. 

Cada partido registra al equipo local, al equipo visita y los goles de cada uno.

```python
partidos = [
    {'local': 'Colo-Colo', 'visita': 'La U',      'goles_local': 3, 'goles_visita': 1},
    {'local': 'La U',      'visita': 'Audax',      'goles_local': 0, 'goles_visita': 0},
    {'local': 'Audax',     'visita': 'Colo-Colo',  'goles_local': 1, 'goles_visita': 2},
    {'local': 'Colo-Colo', 'visita': 'Audax',      'goles_local': 1, 'goles_visita': 1},
    {'local': 'La U',      'visita': 'Colo-Colo',  'goles_local': 2, 'goles_visita': 2},
    {'local': 'Audax',     'visita': 'La U',        'goles_local': 0, 'goles_visita': 3},
]
```

**Las reglas de puntuación son las del fútbol real:**
- Victoria → 3 puntos para el ganador, 0 para el perdedor.
- Empate → 1 punto para cada equipo.

**Lo que debes lograr:**

Construye la tabla de posiciones de la liga desde cero. Al final, imprime los equipos ordenados de mayor a menor puntaje con sus puntos, y declara al campeón.

**Resultado esperado en consola:**
```
1. Colo-Colo — 8 pts
2. La U — 5 pts
3. Audax — 2 pts
Campeón: Colo-Colo
```

**Lo que lo hace difícil:** Este desafío tiene cuatro fases y ninguna es trivial.

**Fase 1 — Registro dinámico:** Al igual que en el desafío anterior, 
debes construir el diccionario de puntos en blanco y agregar equipos dinámicamente. Pero aquí hay dos equipos por partido, así que tienes que hacer ese chequeo dos veces por vuelta de ciclo.

**Fase 2 — Lógica de partido:** Dentro del `for`, 
debes determinar el resultado del partido comparando `goles_local` con `goles_visita` y repartir los puntos correctamente a cada equipo usando los corchetes del diccionario.

**Fase 3 — Ordenamiento manual:** Python tiene `.sort()`, 
pero aquí no lo has visto. Tendrás que ordenar la tabla tú mismo: usando el patrón de búsqueda de máximo que ya conoces, pero repetido para construir una nueva lista ordenada. 
Esta es la parte que más va a hacer pensar.

**Fase 4 — Impresión con posición:** 
Al imprimir, necesitas un contador de posición (1°, 2°, 3°...) que avance junto con el recorrido de la lista ordenada.

Cuatro fases encadenadas, ninguna ayuda en el código, solo los datos. Si llegas al resultado correcto, realmente ya no eres principiante.'''

import time

Contador = 0

Partidos = [

    {'Local': 'Colo-Colo', 'Visita': 'La U',      'Goles_Local': 3, 'Goles_Visita': 1},

    {'Local': 'La U',      'Visita': 'Audax',      'Goles_Local': 0, 'Goles_Visita': 0},

    {'Local': 'Audax',     'Visita': 'Colo-Colo',  'Goles_Local': 1, 'Goles_Visita': 2},

    {'Local': 'Colo-Colo', 'Visita': 'Audax',      'Goles_Local': 1, 'Goles_Visita': 1},

    {'Local': 'La U',      'Visita': 'Colo-Colo',  'Goles_Local': 2, 'Goles_Visita': 2},

    {'Local': 'Audax',     'Visita': 'La U',        'Goles_Local': 0, 'Goles_Visita': 3},

            ]

Cantidad_Puntajes = 0

Lista_de_Scores = []

Puntajes = [

    {'Colo-Colo' : 0},

    {'La U' : 0},

    {'Audax' : 0}

            ]

Resultados_Finales = {

    'Iguales' : 10,

    'Distintos' : 0,

    'Algunos Iguales' : -1

                      }


Categoria_De_Resultado = {

    'Victoria' : 3,

    'Derrota' : 0,

    'Empate' : 1

                         }


for Datos in Partidos:

    time.sleep(0.5)

    print(f'{Datos['Local']} VS {Datos['Visita']} ({Datos['Goles_Local']}-{Datos['Goles_Visita']})')

    if Datos['Goles_Local'] > Datos['Goles_Visita']:

        for X in range(len(Puntajes)):
            
            if Datos['Local'] in Puntajes[X]:

                Puntajes[X][Datos['Local']] += Categoria_De_Resultado['Victoria']

    elif Datos['Goles_Local'] < Datos['Goles_Visita']:

        for X in range(len(Puntajes)):
            
            if Datos['Visita'] in Puntajes[X]:

                Puntajes[X][Datos['Visita']] += Categoria_De_Resultado['Victoria']

    elif Datos['Goles_Local'] == Datos['Goles_Visita']:

        for X in range(len(Puntajes)):
            
            if Datos['Visita'] in Puntajes[X]:

                Puntajes[X][Datos['Visita']] += Categoria_De_Resultado['Empate']

        for X in range(len(Puntajes)):
            
            if Datos['Local'] in Puntajes[X]:

                Puntajes[X][Datos['Local']] += Categoria_De_Resultado['Empate']

for Datucos in Puntajes:

    for Datos in Datucos.values():

        Lista_de_Scores.append(Datos)

Cantidad_de_Veces_que_se_Repite = 0

Alarma = 0

Todos_los_valores_son_Iguales = False

Todos_los_valores_son_Distintos = False

Algunos_son_Iguales = False

Lista_de_Scores.sort(reverse=True)

for X in Lista_de_Scores:

    for Y in range(len(Lista_de_Scores)):

        if X == Lista_de_Scores[Y]:

            Cantidad_de_Veces_que_se_Repite += 1

    if Cantidad_de_Veces_que_se_Repite == 1:

        Alarma += Resultados_Finales['Distintos']

    elif Cantidad_de_Veces_que_se_Repite == len(Lista_de_Scores):

        Alarma += Resultados_Finales['Iguales']

    else: 

        Alarma += Resultados_Finales['Algunos Iguales']

    Cantidad_de_Veces_que_se_Repite = 0

if Alarma == Resultados_Finales['Distintos']:

    Todos_los_valores_son_Distintos = True

elif Alarma == (len(Lista_de_Scores) * Resultados_Finales['Iguales']):

    Todos_los_valores_son_Iguales = True

elif Alarma == (len(Lista_de_Scores) * Resultados_Finales['Algunos Iguales']):

    Algunos_son_Iguales = True

if Todos_los_valores_son_Distintos == True:

    while Cantidad_Puntajes < (len(Puntajes)):

        for Datucos in Puntajes:

            for Llaves, Valores in Datucos.items():

                if Valores == Lista_de_Scores[Cantidad_Puntajes]:
                    
                    print(f'{Cantidad_Puntajes + 1}* {Llaves}')


        Cantidad_Puntajes += 1


elif Todos_los_valores_son_Iguales == True:

    for Datucos in Puntajes:

        for Llaves, Valores in Datucos.items():

            time.sleep(0.5)

            print(f'{Llaves}: {Valores} Puntos')

            Contador += 1

    if Contador == len(Puntajes):

        time.sleep(1)

        print('TODOS EMPATARON! ! !')


elif Algunos_son_Iguales == True:

    print('No hay presupuesto para este calculo')