while True:
    try:
        edad_usuario = int(input("Ingrese su edad en números: "))
        if edad_usuario >= 18:
            print(f"Edad registrada: {edad_usuario} años.")
            break
        elif edad_usuario < 18 and edad_usuario > 0:
            print("Menores de 18 nos son aptos para rentar vehículos")
        else:
            print("Escribir 0 o menor es claramente inválido")
    except ValueError:
        print("Le pedimos, que lo ingrese en números, porfavor vuelva a intentarlo")