#Define el diccionario ventas = {'taza': 500, 'plato': 1200, 'vaso': 300}. 
#Crea una variable total_ventas con valor 0. Recorre los valores del diccionario, súmalos y luego imprime el total.
ventas = {"taza": 500, "plato": 1200, "vaso": 300}
total_ventas = 0 
for venta in ventas.values():
    total_ventas= total_ventas + venta
print(total_ventas)
