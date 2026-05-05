compra_cliente = 25000
region_cliente = "Magallanes"

if compra_cliente > 20000:
    costo_de_envio = 0
else:
    costo_de_envio = 3000

if region_cliente == "Magallanes" or region_cliente == "Aysen":
    costo_de_envio = "2000"


print(costo_de_envio)