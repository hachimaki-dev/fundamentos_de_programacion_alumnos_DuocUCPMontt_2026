print("///////////// TIENDA DE SUPLEMENTOS /////////////")

total_suplemento = 0
cantidad_total_suplemento = 0

continuar = "si"

while continuar == "si":

    precio_suplemento = int(input("¿Cual es el valor de cada pote de proteina?:$"))
    if precio_suplemento <= 0:
        break
    cantidad_suplemento = int(input("¿Cuantos potes de proteina desea llevar?: "))

    total_suplemento += (precio_suplemento * cantidad_suplemento)
    cantidad_total_suplemento += cantidad_suplemento

    print(f"El total a pagar es de ${total_suplemento}")
    print(f"La cantidad total de productos es de: {cantidad_total_suplemento}")
    continuar = input("\n¿Quiere seguir comprando? (si/no):").lower()

if cantidad_total_suplemento >= 3:
    total_suplemento *= 0.9
    print("\n---- Se aplico un descuento del 10% ----")

print(f"El total a pagar es de ${total_suplemento}")
print(f"La cantidad total de productos es de: {cantidad_total_suplemento}\n")
print("Finalizando compras, que tenga buen dia :D")