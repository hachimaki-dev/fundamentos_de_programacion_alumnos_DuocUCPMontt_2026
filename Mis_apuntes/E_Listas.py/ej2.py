productos = [{
    "nombre" : "Carne Asada","precio" : 4990, "Stock" : 5}, {"nombre":"Jugo",
    "precio" : 1490, "Stock": 10}, {"nombre" : "Rábanos","precio" : 990,"Stock" : 15        #SE HABRE 1 DICCIONARIO [{}]
}]

disponibles = 0

for producto in productos:
    print(f"Nombre : {producto["nombre"]}")
    print(f"Precio: {producto["precio"]}")
    print(f"Stock : {producto["Stock"]}")

    if productos["Stock"] > 0:
        print("Disponible.")
        disponibles += 1
    else:
        print("No disponible.")
print(f"Cantidad de productos disponibles : {disponibles}")