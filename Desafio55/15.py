compra_cliente=25000
cliente_vive="Magallanes"
envio=0
if compra_cliente>20000:
    envio=0
elif compra_cliente<20000:
    envio=3000
if cliente_vive=="Magallanes"or "Aysen":
    envio=2000
print(envio)