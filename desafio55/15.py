cliente_productos = 25000
destino = "magallanes"

if cliente_productos > 20000:
    envio = 0
else: 
    envio = 3000
if destino == "magallanes" or "aysen":
    envio = envio + 2000
print("envio")


