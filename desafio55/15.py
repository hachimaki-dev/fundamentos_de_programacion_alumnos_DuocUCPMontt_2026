region= "magallanes"
total_productos= 25000
cargo_zona_extrema= 2000

if total_productos > 20000:
    envio= 0   #Envio gratis
else:
    envio= 3000


if region == "magallanes" or region == "aysen":
    envio= envio + cargo_zona_extrema
    print(f"Tu envio cuesta {envio}")
