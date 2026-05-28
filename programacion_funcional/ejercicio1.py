medicamentos_mensual = 60000
despacho_domicilio = 8000
descuento = 0

edad = int(input("Ingrese su edad: "))
tramo = input("Ingrese su tramo A/B/C/D: ").lower()
if edad <= 30:

    if tramo == "a" or tramo == "b":
        descuento = 0.18
        print("Tienes un descuento del 18%")
        total = medicamentos_mensual * (1 - descuento)
        print(f"Tu total por medicamentos es de {total}")
    elif tramo == "c" or tramo == "d":
        descuento = 0.12
        print("Tienes un descuento del 12%")
        total = medicamentos_mensual * (1 - descuento)
        print(f"Tu total por medicamentos es de {total}")
    else:
        print("Ingresa algo valido")
elif 31 <= edad <= 60:
    if tramo == "a" or tramo == "b":
        descuento = 0.12
        print("Tienes un descuento del 12%")
        total = medicamentos_mensual * (1 - descuento)
        print(f"Tu total por medicamentos es de {total}")
    elif tramo == "c" or tramo == "d":
        descuento = 0.08
        print("Tienes un descuento del 8%")
        total = medicamentos_mensual * (1 - descuento)
        print(f"Tu total por medicamentos es de {total}")
    else:
        print("Ingresa algo valido")
elif edad > 60:
    descuento = 0
    print("Lo siento, no tienes descuentos")
else:
    print("Ingresa algo valido")


if tramo == "a" or tramo == "b":
    descuento_despacho = 0.10
    print("Tienes un descuento en tu despacho del 10%")
    total_despacho = despacho_domicilio * (1 - descuento_despacho)
    print(f"Tu despacho tiene un valor de {total_despacho}")
if edad >= 55:
    descuento_despacho = 0.15
    total_despacho = despacho_domicilio * (1 - descuento_despacho)
    print(f"Tu despacho tiene un valor de {total_despacho}")
else:
    total_despacho = despacho_domicilio
    print("No tienes descuento en tu despacho")
    print(f"Tu despacho tiene el valor de {despacho_domicilio}")