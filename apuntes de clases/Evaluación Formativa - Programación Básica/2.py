total_a_pagar = 0
cantidad_de_productos = 0

print("=======TIENDA DE SUPLEMENTOS=========")
while True :    
    print("elija que suplemento desea comprar")
    print("1. suplemento chico : $5000")
    print("2. suplemento mediano : $7000")
    print("3. suplemento Grande : $10000")
    precio_suplemento = int(input("¿Que precio tiene el suplemento que va a agregar al carrito?(si desea terminar su" \
    " pedido ponga 0 :  "))
    if precio_suplemento < 5000 or precio_suplemento > 10000 :
        break
    elif precio_suplemento == 5000:
        total_a_pagar += 5000
        cantidad_de_productos += 1    
    elif precio_suplemento == 7000:
            total_a_pagar += 7000
            cantidad_de_productos += 1   
    elif precio_suplemento == 10000:
        total_a_pagar += 10000
        cantidad_de_productos += 1   

if cantidad_de_productos >= 3:
    descuento = total_a_pagar * 0.10
    total_a_pagar -= descuento

print(f"El total a pagar por los productos comprados es:   {total_a_pagar} ")
print(f"El total de productos que usted compro son:  {cantidad_de_productos}")