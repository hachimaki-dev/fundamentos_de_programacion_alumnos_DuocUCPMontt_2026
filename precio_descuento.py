total_a_pagar = 0
cantidad_productos = 0
precio = -1
while precio != 0 :
    precio = float(input("Ingrese precio del producto : "))
    print("pulse 0 para terminar")
    if precio != 0:
        total_a_pagar = total_a_pagar + precio
        cantidad_productos + cantidad_productos + 1
if cantidad_productos < 3 :
    total_a_pagar = total_a_pagar * 0.9
print(f"total a pagar es : {total_a_pagar}")
print(f"cantidad de productos {cantidad_productos}")
