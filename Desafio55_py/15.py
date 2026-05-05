en_productos = 25000
vive = "magallanes"
envio = 0

if en_productos > 20000 :
    print("ENVIO NORMAL ES GRATIS")
    envio += 0
elif en_productos < 20000:
    print("ENVIO CUESTA 3000")
    envio += 3000


if vive == "magallanes" or "aysen":
    print("PERO POR VIVIR POR ACA SE LE AGREGAN 2000 EXTRAS AL ENVIO")
    envio += 2000




print(f"EL PRECIO DEL ENVIO ES: {envio}")
