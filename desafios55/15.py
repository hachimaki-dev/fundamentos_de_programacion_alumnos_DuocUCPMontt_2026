compra_cliente = 25000
envio = 3000
envio_extra = 2000
envio_final = ""
region_cliente = "Magallanes"

if compra_cliente > 20000 :
    envio = 0 


else : 
    envio = 3000
    print(envio)

if region_cliente == "Magallanes" or "Aysen" :
    envio = envio + 2000
    print(envio)