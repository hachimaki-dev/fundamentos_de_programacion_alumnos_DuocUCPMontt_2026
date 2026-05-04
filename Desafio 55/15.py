gasto_en_compra = 25000
region = "Magallanes"
costo_envio = 0

costo_total = gasto_en_compra

if gasto_en_compra > 20000 :
    costo_envio = 0
else :
    costo_envio = 3000

if region == "Magallanes" or region == "Aysen" :
    costo_envio += 2000

costo_total = gasto_en_compra + costo_envio

print(costo_envio)