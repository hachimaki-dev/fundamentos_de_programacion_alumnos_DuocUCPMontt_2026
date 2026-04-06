#Tienda de suplementos (con ciclos)

contador_suplementos = 0
precio_producto = 0
continuara_comprando = 0
total_carrito = 0
seguir_comprando = 1


print("###### Bienvenido a nuestra tienda de suplementos ######")

while True:
    if seguir_comprando == 1:
        precio_producto = int(input("¿Cuál es el precio de el primer producto que desea comprar?"))
        contador_suplementos = contador_suplementos + 1
        total_carrito = total_carrito  + precio_producto
        print(f"El total del carrito e momento es {total_carrito}")
        seguir_comprando = int(input("Desea seguir comprando? 1. COntinuar 2. Salir"))
    else:
        print(f"Su precio final del carrito es {total_carrito}")
        break
if contador_suplementos >= 3:
    total_carrito = total_carrito * 1/10
    print(f"Gracias a que su compra ha superado los 2 productos, ha accedido a un 10 por ciento de descuento quedando en ${total_carrito}pesos")
    print("Gracias por preferirnos")
else:
    print("Gracias por preferirnos")

