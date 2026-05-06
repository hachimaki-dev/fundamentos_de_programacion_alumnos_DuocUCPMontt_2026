productos = 25000
region = "magallanes"
costo_envio = 0

if productos >= 20000:
    costo_envio = 0

else:
    costo_envio = costo_envio + 3000

if region == "magallanes" or "aysen":
    costo_envio = costo_envio + 2000

    print(costo_envio)