# Ejercicio 8 — Clasificación de ventas de un local
# Un local de ventas registra los montos de 6 ventas del día. Cada venta es un entero positivo (en pesos).

# Clasifica cada venta con estos rangos exactos:

# Mayor a $50.000 (> 50000) → Venta mayor
# De $10.000 a $50.000 (>= 10000 y <= 50000) → Venta media
# Menor a $10.000 (< 10000) → Venta menor
# Condiciones de borde: Una venta de exactamente $50.000 es "Venta media". Una de exactamente $10.000 también es "Venta media".

# Al final, muestra el conteo de cada tipo y el total recaudado.


while True:

    ventas_mayor = 0
    ventas_media = 0
    ventas_menor = 0
    ventas_totales = 0

    try:

        for numero_de_ventas_diario in range(1,7):
            ventas_registrada = int(input(f"Ingresa la venta N°{numero_de_ventas_diario}: "))

            if ventas_registrada < 0:
                print("La venta debe ser positiva")
                continue

            if ventas_registrada > 50000:
                print("Venta Mayor\n")
                ventas_mayor += 1
            elif ventas_registrada >= 10000 and ventas_registrada <= 50000:
                print("Venta media\n")
                ventas_media += 1
            elif ventas_registrada < 10000:
                print("Venta menor\n")
                ventas_menor += 1
            ventas_totales += ventas_registrada
        
        print("Registro de ventas del dia")
        print(f"Ventas mayor: {ventas_mayor}")
        print(f"Ventas media: {ventas_media}")
        print(f"Ventas menor: {ventas_menor}")
        print(f"Las ventas totales son: ${ventas_totales}")

        break
    
    except ValueError:
        print("Caracter no valido")
        
