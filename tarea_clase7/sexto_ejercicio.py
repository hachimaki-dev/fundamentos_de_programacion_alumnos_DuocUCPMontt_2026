#app delivery kawai
plato1 = 8500
plato2 = 7500
plato3 = 5500
plato4 = 4000
plato5 = 7500
plato6 = 8400
descuento = 10
cantidad_platos = 0
total_a_pagar = 0
while True:
    try:
        opcion_elegida = int(input("Platos disponibles: \n1. Lomo a lo pobre\n2. Lasaña\n3. Canelones de verdura\n4. Canelones de carne\n5. Pastel de papa\n6. Pollo con papas fritas\nIngrese su elección: "))
        if opcion_elegida == 1:
            print(f"Has elegido {opcion_elegida} y su valor es {plato1}")
            total_a_pagar += plato1
            cantidad_platos += 1
        elif opcion_elegida == 2:
            print(f"Has elegido la opción n° {opcion_elegida} y su valor es de {plato2}")
            total_a_pagar += plato2
            cantidad_platos += 1
        elif opcion_elegida == 3:
            print(f"Has elegido la opción n° {opcion_elegida} y su valor es de {plato3}")
            total_a_pagar += plato3
            cantidad_platos += 1
        elif opcion_elegida == 4:
            print(f"Has elegido la opción n° {opcion_elegida} y su valor es de {plato4}")
            total_a_pagar += plato4
            cantidad_platos += 1
        elif opcion_elegida == 5:
            print(f"Has elegido la opción n° {opcion_elegida} y su valor es de {plato5}")
            total_a_pagar += plato5
            cantidad_platos += 1
        elif opcion_elegida == 6:
            print(f"Has elegido la opción n° {opcion_elegida} y su valor es de {plato6}")
            total_a_pagar += plato6
            cantidad_platos += 1
        continuar = int(input("Desea pedir algo más?\n1. Si\n2. No\n: "))
        if continuar == 1:
            continue
        elif continuar == 2:
            break
    except ValueError:
        print("Ingrese una opción valida")


print(f"Has pedido {cantidad_platos} platos en total")
print(f"El total a pagar es de {total_a_pagar}")
descuento = int(total_a_pagar * 0.10)
total_final = total_a_pagar - descuento
if total_a_pagar > 15000:
    print(f"Se aplicara un descuento de 10% a su compra\nEl total ahora es de {total_final}")
elif total_a_pagar < 15000:
    print("No se aplicara ningún descuento.")

print("****Gracias por su compra****")