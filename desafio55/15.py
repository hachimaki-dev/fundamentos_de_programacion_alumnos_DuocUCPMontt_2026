dinero_compra_cliente = 25000
region_cliente = "Magallanes"

if dinero_compra_cliente > 20000:
    precio_envio = 0
else:
    precio_envio = 3000

if region_cliente == "Magallanes" or region_cliente == "Aysen":
    precio_envio = precio_envio + 2000
else:
    pass

print(precio_envio)
