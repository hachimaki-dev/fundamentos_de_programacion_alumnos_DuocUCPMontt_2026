producto_1 = {"Nombre":"Fideos","Precio":900,"Stock":10}
producto_2 = {"Nombre":"Maní","Precio":1000,"Stock":0}
Producto_3 = {"Nombre":"papas","Precio":1000,"Stock":12}
productos = [producto_1 , producto_2, Producto_3]

for precio in productos:
    print(f"{precio["Nombre"]}. Precio: ${precio["Precio"]}")
    if precio["Stock"] > 0:
        print(f"Hay {precio['Stock']} {precio["Nombre"]} disponibles")
    else:
        print(f"Se acabó el stock de {precio['Nombre']}.")    

    