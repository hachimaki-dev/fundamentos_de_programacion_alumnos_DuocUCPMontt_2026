#Define el diccionario:
#tienda = {
#    'pocion': {'precio': 50, 'stock': 3},
#    'espada': {'precio': 200, 'stock': 1}
#}
#Crea una variable capital_total con valor 0. Recorre los productos, multiplica precio × stock para cada uno y suma ese valor al total. Luego, imprime capital_total.
tienda = {
    'pocion': {'precio': 50, 'stock': 3},
    'espada': {'precio': 200, 'stock': 1}
}
capital_total = 0 
for producto in tienda:
    precio = tienda[producto]["precio"]
    stock = tienda[producto]["stock"]
    capital_total += precio * stock

print(capital_total) 