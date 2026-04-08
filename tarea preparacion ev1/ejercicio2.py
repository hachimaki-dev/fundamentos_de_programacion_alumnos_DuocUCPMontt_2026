total_de_compra = 0
contador_productos = 0
boleta = 0
while True:
    valor_producto = int(input(" cauanto vale el producto"))
    if valor_producto == 0:
        break
   
    else:
      total_de_compra = total_de_compra + valor_producto 
      contador_productos = contador_productos + 1

    if contador_productos >= 3:
       boleta = total_de_compra - (total_de_compra * 0.1)

print(f"el total de su boleta es {boleta}")
