compra = 25000
valor_envio = 3000
zona_extrema1 = "magallanes"
zona_extrema2 = "aysen"

vive_en = "magallanes"

if compra > 20000:
    envio = 0
else:
    envio = 3000

if vive_en == zona_extrema1 or vive_en == zona_extrema2:
    envio = envio + 2000

print(envio)