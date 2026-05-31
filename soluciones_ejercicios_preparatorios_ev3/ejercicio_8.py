Dinero_recaudado = 0
Ventas_mayores = 0
Ventas_medias = 0
Ventas_menores = 0
venta_registrada_i = None
for i in range(1,7):
    while True:
        try:
            venta_registrada_i = int(input(f"Ingrese el valor de la venta N°{i}: "))
            if venta_registrada_i <= 0:
                print("Ingrese un valor válido. Un número entero sin comas ni puntos")
            else:
                Dinero_recaudado += venta_registrada_i
                break
        except ValueError:
            print("Ingrese un valor válido. Un número entero sin comas ni puntos")

    if venta_registrada_i > 50000:
        Ventas_mayores += 1
    elif venta_registrada_i >= 10000 and venta_registrada_i <= 50000:
        Ventas_medias += 1
    else:
        Ventas_menores +=1
print(f"Ventas Mayores: {Ventas_mayores}\n Ventas Medias: {Ventas_medias}\n Ventas Menores: {Ventas_menores}\n Total Recaudado: ${Dinero_recaudado}")

    
    
    