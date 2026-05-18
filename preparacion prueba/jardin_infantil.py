mensualidad = 85000
kit = 18000
descuento = 0
descuento_kit = 0

edad = int(input("Ingrese la edad del menor (en meses): "))
nivel = int(input("Ingrese su nivel 1/2/3/4: "))

if edad <= 18:
    if nivel == 1 or nivel == 2:
        descuento = 0.20
        print("Tienes un descuento del 20%!")
    elif nivel == 3 or nivel == 4:
        descuento = 0.13
        print("Tienes un descuento del 13%!")
    else:
        print("Ingresa una opcion valida!")
elif edad >= 19 and edad <= 36:
    if nivel == 1 or nivel == 2:
        descuento = 0.12
        print("Tienes un descuento del 12%!")
    elif nivel == 3 or nivel == 4:
        descuento = 0.07
        print("Tienes un descuento del 7%!")
    else:
        print("Ingresa una opcion valida!")
elif edad > 36:
    descuento = 0
    print("No tienes descuentos...")
total = mensualidad * (1 - descuento)


if nivel == 1 or nivel == 2:
    descuento_kit = 0.10
    print("Tienes un descuento en tu kit del 10%")
    if edad <= 12:
        print("Tienes un descuento adicional del 5%")
        descuento_kit = 0.10 + 0.05
total_mensual = total + kit * (1 - descuento_kit)

print(f"Tu total mensual es {total_mensual}")