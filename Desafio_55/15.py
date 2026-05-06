cliente = 25000
casa_cliente = "magallanes"
envio = 0
if cliente > 20000:
    print("envio gratis")
    envio = 0
else:
    envio = 3000


if casa_cliente == "magallanes" or "aysen":
    envio = envio + 2000

    print(envio)