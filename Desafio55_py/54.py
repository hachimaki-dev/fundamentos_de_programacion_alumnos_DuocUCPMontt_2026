carrito = [{"ITEM" : "mouse" , "qty" : 2 , "precio" : 15000} , {"ITEM" : "teclado" , "qty" : 1 , "precio" : 30000}]

precio_a_pagar = 0

for c in carrito:
    subtotal = c["qty"] * c["precio"]

    precio_a_pagar += subtotal


if precio_a_pagar > 50000:
    precio_a_pagar -= (precio_a_pagar * 0.10)


print(precio_a_pagar)