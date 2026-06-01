cantidad_venta_mayor = 0
cantidad_venta_media = 0
cantidad_venta_menor = 0
total_recaudado = 0

for i in range (1,7):
    while True:
        try:
            ventas_del_dia = int(input(f"Ingrese su venta numero {i} del dia: "))

            if ventas_del_dia <= 0:
                print("¡Dato invalido: Ingrese un valor entero positivo!")

            else:
                total_recaudado += ventas_del_dia
                break

        except ValueError:
            print("¡Dato invalido: Ingrese un valor entero positivo!")
        
    if ventas_del_dia > 50000:
        print("Venta mayor")
        cantidad_venta_mayor += 1

    elif ventas_del_dia >= 10000 and ventas_del_dia <= 50000:
        print("Venta media")
        cantidad_venta_media += 1
        
    else:
        print("Venta menor")
        cantidad_venta_menor += 1

print("---- RESUMEN ----")
print(f"Ventas mayores: {cantidad_venta_mayor}")
print(f"Ventas medias: {cantidad_venta_media}")
print(f"Ventas menores: {cantidad_venta_menor}")
print(f"Total recaudado es de: ${total_recaudado}")