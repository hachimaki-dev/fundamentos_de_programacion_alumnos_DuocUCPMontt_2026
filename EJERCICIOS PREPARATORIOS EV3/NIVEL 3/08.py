#Ejercicio 8 — Clasificación de ventas de un local
#Un local de ventas registra los montos de 6 ventas del día. Cada venta es un entero positivo (en pesos).

#Clasifica cada venta con estos rangos exactos:

#Mayor a $50.000 (> 50000) → Venta mayor
#De $10.000 a $50.000 (>= 10000 y <= 50000) → Venta media
#Menor a $10.000 (< 10000) → Venta menor
#Condiciones de borde: Una venta de exactamente $50.000 es "Venta media". Una de exactamente $10.000 también es "Venta media".

#Al final, muestra el conteo de cada tipo y el total recaudado.

venta_mayor = 0
venta_media = 0
venta_menor = 0

total_ventas = 0

for v in range(6):
    while True:
        try:
            venta_del_dia = int(input(f"Ingresa monto de la venta {v + 1}: "))
            if venta_del_dia > 0:
                break
            else:
                print("Error: la venta debe ser entero positivo, mayor a 0")
        except ValueError:
            print("Error: ingrese un número valido")
    
    if venta_del_dia > 50000:
        venta_mayor += 1
    elif 10000 <= venta_del_dia <=50000:
        venta_media += 1
    else:
        venta_menor += 1
    
    total_ventas += venta_del_dia

print("\n-----------------------------------------")
print(f"Ventas mayores = {venta_mayor}")
print(f"Ventas medias = {venta_media}")
print(f"Ventas menores = {venta_menor}")
print(f"Total recaudado = ${total_ventas}")
print("-----------------------------------------")