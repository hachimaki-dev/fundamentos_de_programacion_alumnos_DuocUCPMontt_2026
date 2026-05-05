
compra = int(input("Ingrese el total de compra: "))

while True: 
    print("1. Los Lagos")
    print("2. Magallanes")
    print("3. Aysen")
    print("4. Salir")

    region = int(input("indique su destino: "))
    if region == 4: 
        break

    if compra > 20000: 
        envio = 0
    else: 
        envio = 3000

    if region == 2 or region == 3: 
        envio = 2000

    print(envio)
    break