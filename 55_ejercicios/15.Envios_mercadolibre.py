total_a_pagar_productos = 25000
region = "Magallanes"
if total_a_pagar_productos > 20000:
    envio = 0
else:
    envio = 3000

if region == "Magallanes" or region == "Aysen":
    envio += 2000
    
print(f"El total del envio es: {envio}")