membresia= 35000
casillero= 4500
descuento= 0
descuento_casillero= 0

plan= int(input("Ingrese su plan 1/2/3/4: "))
meses= int(input("Ingresa la cantidad de meses: "))

if meses >= 12:
    if plan == 1 or plan == 2:
        descuento = 0.22
        print("Tienes un descuento del 22%!")
    elif plan == 3 or plan == 4:
        descuento = 0.15
        print("Tienes un descuento del 15%!")
    else:
        print("Ingresa algo valido")
elif meses >= 6 and meses <= 12:
    if plan == 1 or plan == 2:
        descuento = 0.12
        print("Tienes un descuento del 12%!")
    elif plan == 3 or plan == 4:
        descuento = 0.07
        print("Tienes un descuento del 7%!")
    else:
        print("Ingresa algo valido")
elif meses < 6:
    descuento = 0
    print("No tienes descuento")

total_membresia= membresia * (1 - descuento)
print(total_membresia)

if plan == 1 or plan == 2:
    descuento_casillero = 0.15
    if meses >= 9:
        descuento_casillero = 0.20
        total= total_membresia + casillero * (1 - descuento_casillero)

print(f"Tu total de membresia y casillero es de {total}")