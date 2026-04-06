print("bienvenido")
caja = 0
productos = 0
descuento = 10
while True :
    agregar = int(input("precio del producto a agregar"))
    if agregar == 0 :
        print("salir")
        break
    caja = caja + agregar
    productos = productos + 1

if productos >= 3 :
    final = caja/100*descuento
    caja = caja - final 
    print(f"llevas {productos} productos")
    print(f"al llevar mas de 3 productos se ha hecho un 10% de descurento precio final {caja}")
else :
    print(f"el resultado final es {caja}")
    print(f"has llevado {productos} productos")