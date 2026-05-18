cuenta_mensual= 45000
cargo_medicion= 6000
descuento= 0
descuento_medicion= 0

consumo= int(input("Ingresa el tu consumo mensual en kWh: "))
tarifa= input("Ingresa tu tarifa A/B/C/D: ").upper()
    
if consumo >= 500:
    if tarifa == "A" or tarifa == "B":
        descuento= 0.20
        print("Tienes un descuento del 20%!")
    elif tarifa == "C" or tarifa == "D":    
        descuento= 0.14
        print("Tienes un descuento de 14%!")
    else:
        print("Ingrese algo valido")
elif consumo >= 200 and consumo <= 499:
    if tarifa == "A" or tarifa == "B":
        descuento= 0.12
        print("Tienes un descuento del 12%!")
    elif tarifa == "C" or tarifa == "D":    
        descuento= 0.08
        print("Tienes un descuento del 8%!")
    else:
        print("Ingresa algo valido")
elif consumo < 200:
    descuento = 0
    print("no hay descuento")
else:
    print("Ingrese una opcion valida")

total_mensual= cuenta_mensual * (1 - descuento)
print(f"Tu total mensual es: {total_mensual}")


if tarifa == "A" or tarifa == "B": 
    descuento_medicion = 0.10
    if consumo >= 400:
        descuento_medicion += 0.05

total= total_mensual + cargo_medicion * (1 - descuento_medicion)

print(f"Tu total mensual más la medicion es {total}")