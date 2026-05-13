'''## Desafío 4: El Motor de Descuentos por Categoría 🛒

Una tienda online aplica descuentos distintos según la categoría del producto. Las reglas son:

- `'tecnología'` → 15% de descuento
- `'ropa'` → 25% de descuento
- `'alimentos'` → sin descuento

```python
carrito = [
    {'producto': 'Notebook',  'categoria': 'tecnología', 'precio': 600000},
    {'producto': 'Polera',    'categoria': 'ropa',       'precio': 18000},
    {'producto': 'Pan',       'categoria': 'alimentos',  'precio': 2500},
    {'producto': 'Audífonos', 'categoria': 'tecnología', 'precio': 45000},
    {'producto': 'Jeans',     'categoria': 'ropa',       'precio': 35000},
]
```

**Lo que debes lograr:**

Calcula el precio final de cada producto después de su descuento. Imprime cada producto con su precio original y su precio final. Al terminar, imprime el **total a pagar** por todo el carrito.

**Resultado esperado en consola:**
```
Notebook: 600000 → 510000.0
Polera: 18000 → 13500.0
Pan: 2500 → 2500
Audífonos: 45000 → 38250.0
Jeans: 35000 → 26250.0
Total: 590500.0
```

**Lo que lo hace difícil:** El truco no está en los números: está en que las reglas de descuento están en un diccionario separado que tú debes crear, y dentro del `for` debes consultarlo dinámicamente usando la categoría del producto como llave. Es la primera vez que usas un diccionario como tabla de configuración.'''


Carrito = [

    {'Producto': 'Notebook',  'Categoria': 'Tecnologia', 'Precio': 600000},

    {'Producto': 'Polera',    'Categoria': 'Ropa',       'Precio': 18000},

    {'Producto': 'Pan',       'Categoria': 'Alimentos',  'Precio': 2500},

    {'Producto': 'Audífonos', 'Categoria': 'Tecnologia', 'Precio': 45000},

    {'Producto': 'Jeans',     'Categoria': 'Ropa',       'Precio': 35000},

            ]

Descuentos = {

    'Tecnologia' : 0.85, 
    
    'Ropa' : 0.75, 
    
    'Alimentos' : 1

              }


Carrito_tras_los_Descuentos = [

    {'Producto': 'Notebook',  'Categoria': 'Tecnologia', 'Precio': None},

    {'Producto': 'Polera',    'Categoria': 'Ropa',       'Precio': None},

    {'Producto': 'Pan',       'Categoria': 'Alimentos',  'Precio': None},

    {'Producto': 'Audífonos', 'Categoria': 'Tecnologia', 'Precio': None},

    {'Producto': 'Jeans',     'Categoria': 'Ropa',       'Precio': None},

                                ]

Indicador_indice_Lista_Carritos_Descuentos = 0

for Todos_los_Productos in Carrito:

    if Todos_los_Productos['Categoria'] == 'Tecnologia':

        Carrito_tras_los_Descuentos[Indicador_indice_Lista_Carritos_Descuentos]['Precio'] = Todos_los_Productos['Precio'] * Descuentos['Tecnologia']
            
    elif Todos_los_Productos['Categoria'] == 'Ropa':

        Carrito_tras_los_Descuentos[Indicador_indice_Lista_Carritos_Descuentos]['Precio'] = Todos_los_Productos['Precio'] * Descuentos['Ropa']

    elif Todos_los_Productos['Categoria'] == 'Alimentos':
        
        Carrito_tras_los_Descuentos[Indicador_indice_Lista_Carritos_Descuentos]['Precio'] = Todos_los_Productos['Precio'] * Descuentos['Alimentos']

    Indicador_indice_Lista_Carritos_Descuentos += 1

Total = 0

for Suma_Total in Carrito_tras_los_Descuentos:

    Total += Suma_Total['Precio']
    
for X in range(len(Carrito_tras_los_Descuentos)):

    print(f'{Carrito_tras_los_Descuentos[X]['Producto']} : {Carrito[X]['Precio']}  →  {Carrito_tras_los_Descuentos[X]['Precio']}')

    if X == (len(Carrito_tras_los_Descuentos) - 1):
        print(f"Total: {Total}")
