compra = 25000
destino = "Magallanes"

if compra > 20000:
    envio = 0

else:
    envio = 3000

if destino == "Magallanes" or "Aysen":
    envio += 2000

print(envio)