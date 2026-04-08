Manzanas = 1300
Peras = 990
Zanahorias = 500
opcion = 0
corte = "*"
productos = float("inf")
nombre_producto = input(f"Ingrese que producto es, {corte} para cortar :")
while nombre_producto != corte:
    producto_adquirido = int(input(f"Ingrese la cantidad adquirida de {nombre_producto} : "))
    if producto_adquirido < productos:
        productos = producto_adquirido
        total = nombre_producto
    nombre_producto = input(f"ingrese otro producto {corte} para cortar :")
print(f"Usted lleva {productos} productos y que productos son mas en su canasta : {total}")
print("desea un descuento por la cantidad de su compra? Marque como numero")
match opcion:
    case 1 :
        print("Su descuento sera del 1%")
    case 2 :
        print("Su compra ha finalizado , gracias por comprar")
        exit
