compra = 25000
donde_vive = "magallanes" 
if compra > 20000:
    envio = 0
else:
    envio = 3000

if donde_vive == "magallanes" or "aysen":
    envio = envio + 2000
    print(f"valor de envio es de: {envio}")