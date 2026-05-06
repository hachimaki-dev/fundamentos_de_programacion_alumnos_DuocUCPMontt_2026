monto_compra = 25000
region = "magallanes"
costo_envio = 0

if monto_compra > 20000:
    costo_envio = 0 
else:
    costo_envio = 3000

if region == "magallanes" or region == "aysen":
    costo_envio = costo_envio + 2000

print(f"el costo del envio sera de: {costo_envio}")
