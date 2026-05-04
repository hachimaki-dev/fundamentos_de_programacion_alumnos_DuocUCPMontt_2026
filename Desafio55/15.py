compra = 25000
residencia = "Magallanes"

if compra > 20000:
    envio = 0
else:
    envio = 3000

if residencia == "Magallanes" or residencia == "Aysen":
    envio += 2000

print(envio)