dcto_tecnologia = .15
dcto_ropa = .25
dcto_alimento = 0

total = 0

carrito = [
    {'producto': 'Notebook',  'categoria': 'tecnología', 'precio': 600000},
    {'producto': 'Polera',    'categoria': 'ropa',       'precio': 18000},
    {'producto': 'Pan',       'categoria': 'alimentos',  'precio': 2500},
    {'producto': 'Audífonos', 'categoria': 'tecnología', 'precio': 45000},
    {'producto': 'Jeans',     'categoria': 'ropa',       'precio': 35000},
]

precios_original = []

for item in carrito:
    precios_original.append(item.get("precio"))

carrito_descuento = carrito

indice = -1
for item in carrito:
    indice += 1
    match(item.get("categoria")):
        case "tecnología":
            carrito_descuento[indice]["precio"] -= (item.get("precio") * dcto_tecnologia)
            continue
        case "ropa":
            carrito_descuento[indice]["precio"] -= (item.get("precio") * dcto_ropa)
            continue
        case "alimentos":
            carrito_descuento[indice]["precio"] -= (item.get("precio") * dcto_alimento)
            continue
        case _:
            print("Error")
            continue

indice = -1
for item in carrito:
    indice += 1
    print(f"{item.get("producto")}: {precios_original[indice]} -> {carrito_descuento[indice].get("precio")}")

for item in carrito_descuento:
    total += item.get("precio")

print(f"Total: {total}")