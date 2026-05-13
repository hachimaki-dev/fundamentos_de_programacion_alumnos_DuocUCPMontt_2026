'''
## Desafío 6: El Sistema de Reputación ⭐

Una plataforma de servicios como Airbnb guarda las reseñas que los usuarios le dejan a cada anfitrión. Cada reseña tiene el nombre del anfitrión y una nota del 1 al 5.

```python
resenas = [
    {'Anfitrion': 'Mario',   'Nota': 5},
    {'Anfitrion': 'Claudia', 'Nota': 3},
    {'Anfitrion': 'Mario',   'Nota': 4},
    {'Anfitrion': 'Claudia', 'Nota': 5},
    {'Anfitrion': 'Mario',   'Nota': 2},
    {'Anfitrion': 'Claudia', 'Nota': 4},
    {'Anfitrion': 'Mario',   'Nota': 5},
]
```

**Lo que debes lograr:**

Recorre la lista una sola vez y construye, al mismo tiempo, dos diccionarios: uno llamado `totales` que acumule la suma de notas por anfitrión, 
y otro llamado `conteos` que lleve la cuenta de cuántas reseñas tiene cada uno. Ambos deben empezar vacíos y llenarse dinámicamente dentro del `for`.

Una vez terminado el recorrido, calcula el promedio de cada anfitrión dividiendo su total entre su conteo. 

Imprime el promedio de cada uno redondeado a 2 decimales y, al final, imprime quién tiene la mejor reputación.

**Resultado esperado en consola:**
```
Mario: 4.0
Claudia: 4.0
Empate en reputación
```

> **Nota:** Sí, en este caso específico hay empate. 

Tu código debe detectarlo y manejarlo. 

Si no hubiera empate, debería imprimir al ganador con su promedio.

**Lo que lo hace difícil:** Aquí no te damos la estructura de los diccionarios lista. 

Tú debes inicializar las llaves dinámicamente: antes de sumar, 
tienes que revisar si el anfitrión ya existe en el diccionario; 
si no existe, crearlo con valor inicial. 

Es el patrón más importante en el manejo de datos agrupados, 
y para resolverlo necesitas coordinar dos diccionarios en paralelo dentro del mismo ciclo, 
más un segundo recorrido para calcular promedios y detectar empates. Son más de seis decisiones de lógica en cadena.'''


Reseña = [

    {'Anfitrion': 'Mario',   'Nota': 5},

    {'Anfitrion': 'Claudia', 'Nota': 3},

    {'Anfitrion': 'Mario',   'Nota': 4},

    {'Anfitrion': 'Claudia', 'Nota': 5},

    {'Anfitrion': 'Mario',   'Nota': 2},

    {'Anfitrion': 'Claudia', 'Nota': 4},

    {'Anfitrion': 'Mario',   'Nota': 5},

          ]

Personas_Registradas = {

        'Persona 1' : "Mario",

        'Persona 2' : "Claudia"

                        }
Cantidad = {

    'Cantidad Mario' : 0,

    'Cantidad Claudia' : 0
           
           }

Totales = {

    'Total Mario' : 0,

    'Total Claudia' : 0

            }

Promedios = {

    'Promedio Mario' : 0,

    'Promedio Claudia' : 0

            }

for Persona in Reseña:

    if Persona['Anfitrion'] == Personas_Registradas['Persona 1']:

        Cantidad['Cantidad Mario'] += 1

        Totales['Total Mario'] += Persona['Nota']

    elif Persona['Anfitrion'] == Personas_Registradas['Persona 2']:

        Cantidad['Cantidad Claudia'] += 1

        Totales['Total Claudia'] += Persona['Nota']

Promedios['Promedio Mario'] = (Totales['Total Mario']/Cantidad['Cantidad Mario'])
Promedios['Promedio Claudia'] = (Totales['Total Claudia']/Cantidad['Cantidad Claudia'])

print(f'Mario : {Promedios["Promedio Mario"]}')

print(f'Claudia : {Promedios["Promedio Claudia"]}')

if Promedios['Promedio Mario'] == Promedios['Promedio Claudia']:

    print('Empate ! ')
    
elif Promedios['Promedio Mario'] > Promedios['Promedio Claudia']:

    print(f'El Ganador es: {Personas_Registradas["Persona 1"]}')

elif Promedios['Promedio Mario'] < Promedios['Promedio Claudia']:

    print(f'El Ganador es: {Personas_Registradas["Persona 2"]}')