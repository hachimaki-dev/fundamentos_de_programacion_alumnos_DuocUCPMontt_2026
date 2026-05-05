compra_c = 25000 
c_vive = "Magallanes"
envio = 0

if compra_c > 20000:
    envio = 0
    if c_vive == "Magallanes" or "Aysen":
        envio += 2000
        print(envio)
elif compra_c < 20000:
    envio = 3000
    if c_vive == "Magallanes" or "Aysen":
        envio += 2000
        print(envio)
