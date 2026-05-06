compra_cliente =  25000
hogar_cliente = "Magallanes"
coste_envio = 0

if compra_cliente >= 20000:
    print("El envio normal es gratis")
else:
    print("El envio cuesta $3000")
    coste_envio += 3000

if hogar_cliente == "Magallanes" or "Aysen":
    print("Se añadira un costo adicional al envio debido a ser una zona extrema.")
    coste_envio += 2000
else:
    print("No se añadira ningún coste extra al envio.")

print(f"Su pedido llegara lo más breve posible, el costo del envio es de {coste_envio}")