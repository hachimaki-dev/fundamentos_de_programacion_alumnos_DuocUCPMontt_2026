productos = 25000

region = "magallanes"

if productos > 20000:
    envio = 0
else:
    envio = 3000

if region == "magallanes" or region == "aysen":
    envio += 2000


print(envio)

