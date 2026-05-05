gasto_en_productos = 25000
localidad = input("Ingrese su localidad")
envio_extra = 2000
envio = 0
if gasto_en_productos > 20000 and localidad == "Magallanes" or localidad == "Aysen":
    envio = envio + envio_extra
elif gasto_en_productos > 20000 and localidad != "Magallanes" and localidad != "Aysen":
    envio = 0
if gasto_en_productos <= 20000 and localidad == "Magallanes" or localidad == "Aysen":
    envio = 3000
    envio = envio + envio_extra
elif gasto_en_productos <= 20000 and localidad != "Magallanes" and localidad != "Aysen":
    envio = 3000

print(envio)