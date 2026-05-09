'''Ejercicio 38: Top 3 Ventas (MercadoLibre)
Muestra los 3 productos más vendidos de tu tienda virtual.

Datos Iniciales: Tus productos vendieron estas cantidades: `[500, 1000, 200, 800, 1500]`.

Reglas de Negocio: Para mostrar un 'Top 3', primero necesitas ordenar los números del más grande al más chico. 

Luego, simplemente recortas los primeros 3 y descartas el resto.

Restricciones: Ordena la lista de mayor a menor usando `.sort(reverse=True)`. 

Después, usa la técnica de rebanado de listas (slicing) escribiendo `[:3]` para atrapar solo a los ganadores. Imprime esa rebanada.'''

Precio_Productos_Vendidos = [500, 1000, 200, 800, 1500]

Precio_Productos_Vendidos.sort(reverse=True)

print(f'[{Precio_Productos_Vendidos[0]}, {Precio_Productos_Vendidos[1]}, {Precio_Productos_Vendidos[2]}]')