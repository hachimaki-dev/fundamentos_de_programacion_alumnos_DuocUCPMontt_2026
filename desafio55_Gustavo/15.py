cliente = 25000
zona = "Magallanes"
envio = 0

if cliente > 20000 :
    envio = 0
else :
    envio = 3000

if zona == "Magallanes" or "Aysen":
    envio = 2000

print(envio)