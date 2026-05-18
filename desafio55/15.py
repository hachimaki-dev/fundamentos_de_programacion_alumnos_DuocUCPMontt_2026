cliente_compra_productos = 25000
destino = "Magallanes"
if cliente_compra_productos > 20000:
    costo_envio = 0
else:
    costo_envio = 3000
if destino == "Magallanes" or "Aysen":
    costo_envio = costo_envio + 2000
print(costo_envio)

