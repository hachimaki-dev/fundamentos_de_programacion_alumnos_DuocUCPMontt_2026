compra_cliente = 250000
region_cliente = "magallanes"
costo_Extra = 2000
if region_cliente == "magallanes" or "aysen":
    compra_cliente = compra_cliente + costo_Extra
    print(f"el costo de envio es de {costo_Extra}")
if compra_cliente > 200000 and region_cliente != "magallanes" or "aysen" == True:
    print("envio gratis")
else:
    print("se añadira el costo extra por la region")