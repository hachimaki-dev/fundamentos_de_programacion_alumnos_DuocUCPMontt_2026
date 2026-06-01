venta_alta = 0
venta_media = 0
venta_baja = 0
total = 0

for i in range(1,7):
    ingresos_diarios = int(input(f"Ingresa las ganancias del dia {i}: "))

    if ingresos_diarios > 50000:
        venta_alta += 1
        total = total + ingresos_diarios

    elif ingresos_diarios >= 10000 and ingresos_diarios <= 50000:
        venta_media += 1
        total = total + ingresos_diarios
    
    else:
        venta_baja += 1
        total = total + ingresos_diarios

print("\nResumen de ventas")
print(f"-Ventas altas: {venta_alta}")
print(f"-Ventas medias: {venta_media}")
print(f"-Ventas bajas: {venta_baja}")
print(f"Tu ganancias totales fueron de {total}")