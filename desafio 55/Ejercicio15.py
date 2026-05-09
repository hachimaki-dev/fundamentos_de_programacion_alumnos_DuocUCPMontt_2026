compra = 25000
region = "Magallanes"

if compra >= 20000:
    envio = 0
else:
    envio = 3000
if region == "Magallanes" or region == "Aysen":
    envio = envio + 2000

print(envio)