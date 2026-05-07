#Muestra los 3 productos más vendidos de tu tienda virtual.

#Datos Iniciales: Tus productos vendieron estas cantidades: `[500, 1000, 200, 800, 1500]`.

#Reglas de Negocio: Para mostrar un 'Top 3', primero necesitas ordenar los números del más grande al más chico. Luego, simplemente recortas los primeros 3 y descartas el resto.

#Restricciones: Ordena la lista de mayor a menor usando `.sort(reverse=True)`. Después, usa la técnica de rebanado de listas (slicing) escribiendo `[:3]` para atrapar solo a los ganadores. Imprime esa rebanada.
productos = [ 500 , 1000, 200, 800, 1500]
productos.sort(reverse=True)
print(productos[:3])


