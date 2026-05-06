productos = 25000
ubicacion = "Magallanes, Aysen"
envio_normal = 3000
if productos > 20000 and ubicacion == "Magallanes, Aysen":
  productos = 0
  productos = productos + 2000
  print(productos)
else:
  print(envio_normal)
  
