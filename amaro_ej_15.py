compra_cliente = 25000
region = "Magallanes"
envio_zona_extrema = 2000

if compra_cliente > 20000:
    envio_normal = 0
    print(envio_normal)
    if region == "Magallanes" or region == "Aysen":
        print(envio_zona_extrema)
else:
    compra_cliente = 3000
    print(compra_cliente)