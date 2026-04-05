#taquilla de cine kawaii

print("****Bienvenido a Cinepolis****\nAqui puedes comprar entradas para la pelicula The Super Mario Galaxy")
print("El precio de la entrada varia según su edad")
entradas_compradas = 0
entrada_normal = 6000
entrada_adulto_mayor = 4000
entrada_niños = 3000
total_a_pagar = 0

while True:
    try:
        opcion_elegida = int(input("Que edad tiene?: "))
        if opcion_elegida >= 64:
            print(f"Se le aplicara la tarifa de adulto mayor\nEl precio de la entrada es de {entrada_adulto_mayor}")
            entradas_compradas += 1
            total_a_pagar += entrada_adulto_mayor
        elif opcion_elegida >= 12:
            print(f"Se le aplicara la tarifa regular, su valor es de {entrada_normal}")
            entradas_compradas += 1
            total_a_pagar += entrada_normal
        elif opcion_elegida <= 12:
            print(f"Se le aplicara la tarifa de niños, su valor es de {entrada_niños}")
            entradas_compradas += 1
            total_a_pagar += entrada_niños
        continuar = int(input("Desea comprar otra entrada?\n1. Si\n2. No\n: "))
        if continuar == 1:
            continue
        elif continuar ==2:
            break
        else:
            print("Ingrese una opción valida")
    except ValueError:
        print("Ingrese una opción valida")

print(f"Has comprado {entradas_compradas} entradas en total\nEl precio es de ${total_a_pagar}")

print("Gracias por usar nuestros servicios.")