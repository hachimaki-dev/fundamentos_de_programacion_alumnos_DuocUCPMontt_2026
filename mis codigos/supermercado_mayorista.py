# INCOMPLETO PERO CASI


print("===== SUPERMERCADO MAYORISTA =====")

producto_estrella = input("cual es el producto estrella del dia?:")

precio_unitario_producto_estrella = float(input("cual es el precio unitario del producto?:"))

unidades_producto_estrella = int(input("cuantas unidades lleva?:"))

precio_producto10 = precio_unitario_producto_estrella  * 0.10
precio_producto20 = precio_unitario_producto_estrella * 0.20

precio_unitario_producto_estrella10 = precio_unitario_producto_estrella - precio_producto10
precio_unitario_producto_estrella20 = precio_unitario_producto_estrella - precio_producto20

while True:
    if unidades_producto_estrella < 5:
        print("precio sin oferta")

    elif unidades_producto_estrella > 5 or unidades_producto_estrella == 10:
        print("OFERTA ESPECIAL ACTIVADA, 10% DE DESCUENTO")
        print(f"el precio total es de ${precio_producto10}")

    elif unidades_producto_estrella > 10:
        print("OFERTA ESPECIAL ACTIVADA, 20% DE DESCUENTO")
        print(f"el precio total es de ${precio_producto20}")
    break
    