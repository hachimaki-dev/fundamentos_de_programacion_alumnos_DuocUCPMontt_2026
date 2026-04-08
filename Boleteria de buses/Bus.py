nombre_destino_1 = "Puerto Varas"
nombre_destino_2 = "Frutillar"
nombre_destino_3 = "Osorno"

precio_destino_1 = 3000
precio_destino_2 = 5000
precio_destino_3 = 7000

total = 0
seguir_vendiendo = False

print("---Bienvenido/a a Cruz del sur---")

while = True:
    continuar = int(input()) 
    print("Elija su destino 🚌")
    print("     1. Puerto Varas: $3000")
    print("     2. Frutillar: $5000")
    print("     3. Osorno: $7000")

opcion_seleccionada = int(input("Ingrese su destino:  \n"))

if opcion_seleccionada == 1:
    print(f"Has seleccionado Puerto Varas \n El costo es:\n 1. Pasaje de ida: ${precio_destino_1}\n 2. Pasaje de ida y vuelta: ${precio_destino_1 * 2}")
    
    tipo_viaje = int(input("¿Va de ida? o ¿De ida y vuelta?\n"))
    if tipo_viaje == 1:
        print(f"Ha elegido de ida\n Su subtotal es: ${precio_destino_1}")
    elif tipo_viaje == 2:
         print(f"Ha elegido de ida y vuelta\n Su subtotal es: ${precio_destino_1 * 2}")
    else:
        print("Por favor escoga entre 1 o 2 😊")
elif opcion_seleccionada == 2:
    print(f"Has seleccionado Frutillar \n El costo es:\n 1. Pasaje de ida: ${precio_destino_2}\n 2. Pasaje de ida y vuelta: ${precio_destino_2 * 2}")
elif opcion_seleccionada == 3:
    print(f"Has seleccionado Osorno \n El costo es:\n 1. Pasaje de ida: ${precio_destino_3}\n 2. Pasaje de ida y vuelta: ${precio_destino_3 * 2}")