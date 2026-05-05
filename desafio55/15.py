region = "magallanes"
compra_cliente = 25000
envio_normal = 3000
if compra_cliente >= 20000:
    envio_normal = 0
elif compra_cliente < 20000:
    envio_normal = 3000
if (region == "magallanes" or "aysen") and compra_cliente >= 20000:
    envio_normal = 0
    envio_normal += 2000
elif (region == "magallanes" or "aysen") and compra_cliente < 20000:
    envio_normal += 2000
print(envio_normal)

