costo_productos=25000 #envio para Magallanes
costo_envio=0
costo_envio_extra_zona_extrema=3000
lugar_envio="Magallanes"

if costo_productos > 20000:
    costo_envio=0
    if lugar_envio=="Magallanes" or lugar_envio=="Aysen":
        costo_envio=costo_envio+2000
        print(costo_envio)
    else:
        print(costo_envio)
else:
    costo_envio=costo_envio+3000
    if lugar_envio=="Magallanes" or lugar_envio=="Aysen":
        costo_envio=costo_envio+2000
        print(costo_envio)
    else:
        print(costo_envio)
    

