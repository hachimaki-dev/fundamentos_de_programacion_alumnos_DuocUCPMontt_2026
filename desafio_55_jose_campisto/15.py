compra=25000 
region="Magallanes"
envio=0
if compra >20000 and region != "Magallanes":
    print(envio)
elif compra > 20000 and region == "Magallanes":
    envio+=2000
    print(envio)
else:
    envio+3000
    print(envio)