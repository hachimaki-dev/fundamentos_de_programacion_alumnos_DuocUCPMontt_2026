print("Bienvenido a la consesionaria para arriendo de autos, deberas contarnos tu edad para arrendar un auto.")
keke = True

while keke == True:
    try:
        edad_usuario = int(input("Ingresa tu edad: "))

        if edad_usuario > 0:
            print(f"Muy bien!, entonces tienes {edad_usuario}, puedes arrendar un auto.")
            keke = False
        else:
            print("Ingresa un número mayor a 0")
            continue

    except ValueError:
        print("Ingresa un valor valido y solamente en NÚMEROS ENTEROS.")
        continue