'''

## Desafío 1: El Clasificador de Torneos 🎮

Tienes una lista de jugadores que participaron en un torneo. Cada jugador es un diccionario con su nombre y su puntaje final.

```python
jugadores = [
    {'nombre': 'Nico',   'puntaje': 4200},
    {'nombre': 'Valeria','puntaje': 8750},
    {'nombre': 'Diego',  'puntaje': 3100},
    {'nombre': 'Camila', 'puntaje': 8750},
    {'nombre': 'Matías', 'puntaje': 6300},
]
```

**Lo que debes lograr:**

Recorre la lista y clasifica a cada jugador según su puntaje en una de tres categorías: `'Bronce'` (menos de 5000), `'Plata'` (entre 5000 y 7999), u `'Oro'` (8000 o más). Al final, imprime cuántos jugadores hay en cada categoría.

**Resultado esperado en consola:**
```
Bronce: 2
Plata: 1
Oro: 2
```

**Lo que lo hace difícil:** Necesitas un diccionario de contadores que empiece en cero, un `for` para recorrer jugadores, condicionales para clasificar, y actualizar el conteo en cada vuelta. Son cuatro piezas que deben funcionar juntas.

'''

Jugadores = [

    {'Nombre': 'Nico',   'Puntaje': 4200},

    {'Nombre': 'Valeria','Puntaje': 8750},

    {'Nombre': 'Diego',  'Puntaje': 3100},

    {'Nombre': 'Camila', 'Puntaje': 8750},

    {'Nombre': 'Matías', 'Puntaje': 6300},

            ]

Categorias = {'Bronce' : 0, 'Plata' : 0, 'Oro' : 0}

for Datos in Jugadores:

    print(f'Nombre: {Datos['Nombre']}, Puntaje: {Datos['Puntaje']}')

    if Datos['Puntaje'] < 5000:

        Categorias['Bronce'] += 1

    elif Datos['Puntaje'] >= 5000 and Datos['Puntaje'] <= 7999:

        Categorias['Plata'] += 1

    elif Datos['Puntaje'] >= 8000:

        Categorias['Oro'] += 1

print(f'Bronce: {Categorias['Bronce']}')

print(f'Plata: {Categorias['Plata']}')

print(f'Oro: {Categorias['Oro']}')