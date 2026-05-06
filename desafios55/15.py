monto_compra = 25000
region_destino = "Magallanes"

monto_envio_gratis = 20000
costo_envio_normal = 3000
recargo_zona_extrema = 2000

if monto_compra > monto_envio_gratis:
    costo_envio = 0
else:
    costo_envio = costo_envio_normal

if region_destino == "Magallanes" or region_destino == "Aysen":
    costo_envio = costo_envio + recargo_zona_extrema

print(f"El costo de envio es de {costo_envio}")