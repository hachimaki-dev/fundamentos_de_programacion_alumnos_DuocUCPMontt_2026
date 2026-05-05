compro = 25000 
region = "Magallanes"
zona_extrema = 2000
envio = 0

if compro > 20000:
    envio == 0
else:
    compro < 20000
    envio += 3000

if region == "Magallanes" or "Aysen":
    envio = envio + zona_extrema

print(f"El total del envio es de: {envio}")
