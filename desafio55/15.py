productos = 25000
ubicacion = "Magallanes"
envio_normal = 3000
if productos > 20000 and ubicacion == "Magallanes":
  productos = 0
  productos = productos + 2000
  print(productos)
else:
  print(envio_normal)
  
