compra_cliente = 25000
vive_region = "Magallanes"

if compra_cliente > 20000:
    envio_normal = 0
    if compra_cliente < 20000:
        envio_normal = 3000
if vive_region:
    extra = envio_normal + 2000
    total = envio_normal + extra
print(total)