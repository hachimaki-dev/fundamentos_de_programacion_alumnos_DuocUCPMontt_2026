# El cliente compró 25000
#vive en la región de 'Magallanes'

valor_compra = 25000
destino = "Magallanes"

if valor_compra > 20000:
    costo_envio = 0
else:
    costo_envio = 3000
if destino == "Magallanes" or destino == "Aysen":
    costo_envio = costo_envio + 2000

print(costo_envio)