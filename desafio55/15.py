total_compra = 25000
costo_envio = 0
destino = "Magallanes"


if total_compra > 20000:
    costo_envio = 0

else:
    costo_envio = costo_envio + 3000


if destino == "Magallanes" or destino == "Aysen":
    costo_envio = costo_envio + 2000
    print(costo_envio)