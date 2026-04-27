# TERMINADO

print("========== TIENDA DE SUPLEMENTOS ==========")

while True:
    
    producto = int(input("\n¿Cuánto cuesta el producto? (Escribe 0 para salir): "))

    if producto == 0:
        print("¡Hasta pronto!")
        break

    unidades = int(input("¿Cuántas unidades desea llevar?: "))

    subtotal = producto * unidades

    if unidades > 3:
        print("¡OFERTA ESPECIAL ACTIVADA, 10% DE DESCUENTO!")
        descuento = subtotal * 0.10
        precio_final = subtotal - descuento
        print(f"El precio total con descuento es: ${precio_final}")
    
    elif unidades > 0:
        print("Precio sin descuento.")
        print(f"El precio total es: ${subtotal}")
    
    else:
        print("Cantidad de unidades inválida, intente de nuevo.")