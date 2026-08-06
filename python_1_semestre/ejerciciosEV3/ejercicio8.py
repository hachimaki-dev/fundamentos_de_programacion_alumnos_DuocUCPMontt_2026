""" Ejercicio 8 — Clasificación de ventas de un local
Un local de ventas registra los montos de 6 ventas del día. Cada venta es un entero positivo (en pesos).

Clasifica cada venta con estos rangos exactos:

Mayor a $50.000 (> 50000) → Venta mayor
De $10.000 a $50.000 (>= 10000 y <= 50000) → Venta media
Menor a $10.000 (< 10000) → Venta menor
Condiciones de borde: Una venta de exactamente $50.000 es "Venta media". Una de exactamente $10.000 también es "Venta media".

Al final, muestra el conteo de cada tipo y el total recaudado. """

dia = 1
venta_mayor = 0
venta_media = 0
venta_menor = 0
Total = 0

while dia < 7:
    try:
        ventas = int(input(f"ingresa las ventas del dia {dia} : "))
        if ventas > 50000:
            venta_mayor +=1
            dia +=1 #cuidado con las sumas de variables no es lo mismo += 1 que suman a esa variable que =+ 1 que se le asigana la suma de 1 y se queda ahi
            Total += ventas
            
        elif ventas >= 10000 and ventas <= 50000:
            venta_media +=1
            dia +=1
            Total += ventas
        
        elif ventas < 10000:
            venta_menor +=1
            dia +=1
            Total += ventas
    
    except ValueError:
        print("ingresa un numero entero valido")   

print(f" la cantidad de ventas mayor fue: {venta_mayor}\n la cantidad de ventas medias fue: {venta_media}\n la cantidad de ventas menor fue : {venta_menor}") 
print(f"la cantidad total reunida fue de {Total}")