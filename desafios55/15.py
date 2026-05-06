compra = 25000
region = "magallanes"
envio = 0 if compra > 20000 else 3000
if region in ['magallanes', 'Aysen']:
    envio += 2000
print(envio)