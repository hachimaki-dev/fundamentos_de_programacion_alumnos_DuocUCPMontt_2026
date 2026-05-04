compra = 25000
destino = "magallanes"
envio = ""
if compra > 20000:
    envio = 0
elif compra < 20000:
    envio = 3000


if destino == "magallanes" or "aysen":
    envio = envio + 2000


print(envio)

