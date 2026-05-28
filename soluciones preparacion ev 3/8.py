contador_venta_mayor = 0
contador_venta_media = 0
contador_venta_baja = 0

valor_total_ventas = 0

for i in range(1, 7) :
    while True :
        try :
            valor_venta = int(input(f"Ingrese el precio de la venta {i}: "))

            if valor_venta < 0 :
                print("Ingrese un valor positivo.")
                continue

            if valor_venta < 10000 :
                contador_venta_baja += 1
            elif valor_venta >= 10000 and valor_venta <= 50000 :
                contador_venta_media += 1
            elif valor_venta > 50000 :
                contador_venta_mayor += 1

            valor_total_ventas += valor_venta
            break
        except ValueError :
            print("Ingrese un valor numérico (entero).")
        
print(f"Ventas mayores: {contador_venta_mayor}")
print(f"Ventas medias: {contador_venta_media}")
print(f"Ventas bajas: {contador_venta_baja}")

print(f"Total recaudado: {valor_total_ventas}")