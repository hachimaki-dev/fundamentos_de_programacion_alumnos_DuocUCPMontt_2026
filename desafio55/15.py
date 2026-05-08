compra = 25000
region = "Magallanes"
envio = 0

if compra >= 20000:
    envio = 0
else:
    envio = 3000

if region == ("Magallanes" or "Aysen"):
    envio = envio + 2000
print(envio)