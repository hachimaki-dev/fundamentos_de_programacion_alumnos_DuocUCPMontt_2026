#Crea una lista llamada productos que contenga al menos 3 diccionarios. Cada diccionario debe tener:

#nombre
#precio
#stock

#Luego:

#Recorre la lista con for.
#Muestra el nombre y precio de cada producto.
#Usa if para indicar cuáles productos tienen stock mayor que 0.
#Al final, imprime cuántos productos están disponibles.





lacteos = {
    "nombre" : "Leche",
    "precio" : 1000,
    "stock" : 15

}

legumbres = {
    "nombre" : "Lentejas",
    "precio" : 1500,
    "stock" : 0

}

verduras = {
    "nombre" : "Zapallo",
    "precio" : 900,
    "stock" : 20

}

for clave, valor in lacteos, legumbres, verduras.items():
    print(clave, valor)