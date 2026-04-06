total = 0
contador = 0
subtotal = 0
descuento = 0


while True:
    try:
        suplemento = int(input("Ingresa el precio del suplemento:"))
        subtotal += suplemento
        
        if suplemento < 0:
            print("Ingresa un monto valido.")
            continue
        elif suplemento == 0:
            break
        contador += 1 
        print(f"El producto {contador} vale ${suplemento}")
        
    except ValueError:
        print("Ingresa solo números enteros.")

print(f"Compraste {contador} productos y el subtotal es {subtotal}")
if contador >= 3:
    descuento = subtotal * 0.10
    print(f"Se aplicara un descuento del 10%, el precio a pagar es {subtotal - descuento}")
else:
    print("No se aplicara ningún descuento.")    
    