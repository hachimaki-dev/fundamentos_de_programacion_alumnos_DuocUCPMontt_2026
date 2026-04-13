total_a_pagar = 0
descuento = 0 
precio_producto = 0
productos_que_lleva = 0
deseas_comprar = input("quieres comprar?")
if deseas_comprar != "no": 
    while True:
        precio_producto = int(input("ingrese el valor del producto\nprecione 0 para salir:"))
        total_a_pagar = precio_producto + total_a_pagar
        productos_que_lleva = productos_que_lleva + 1 
        if precio_producto == 0:
            break
if productos_que_lleva >= 3: 
    descuento = total_a_pagar * 0.10
    total_a_pagar = total_a_pagar - descuento

    print(f"su descuento es de {descuento}")
    print(f"usted lleva {productos_que_lleva} de productos")
    print(f"su total a pagar es {total_a_pagar}")
    print("gracias!!!")
else:
    print("hasta luego!!")