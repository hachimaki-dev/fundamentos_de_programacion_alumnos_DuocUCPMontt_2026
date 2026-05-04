valortotalcliente=25000
destino= "Magallanes"
envio = 3000
if valortotalcliente > 20000:
    envio = 0 #envio gratis
else:
    envio = envio
if destino == "Magallanes" or destino == "Aysen": #Zonas extremas
    envio += 2000
print (envio)