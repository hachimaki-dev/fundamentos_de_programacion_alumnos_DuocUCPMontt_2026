compra = 25000
cliente_region = "Magallanes"

if compra > 20000:
    print("No paga envio")
else:
    envio = 3000

if cliente_region == "Magallanes" or "Aysen":
    envio = 2000
print(f"El precio del envio es de {envio}.")