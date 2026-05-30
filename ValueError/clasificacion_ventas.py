# Un local de ventas registra los montos de 6 ventas del día. Cada venta es un entero positivo (en pesos).

# Clasifica cada venta con estos rangos exactos:

# Mayor a $50.000 (> 50000) → Venta mayor
# De $10.000 a $50.000 (>= 10000 y <= 50000) → Venta media
# Menor a $10.000 (< 10000) → Venta menor
# Condiciones de borde: Una venta de exactamente $50.000 es "Venta media". Una de exactamente $10.000 también es "Venta media".

# Al final, muestra el conteo de cada tipo y el total recaudado.
total_recaudado = 0
contador_ventas_diarias = 0
while contador_ventas_diarias <= 5:
    try:
        venta_realizada = int(input("Ingrese el monto de la venta \n"))
        if venta_realizada > 50000:
            print("Venta mayor")
        elif venta_realizada >= 10000 and venta_realizada <= 50000:
            print("Venta media")
        elif venta_realizada < 10000:
            print("Venta menor")
        total_recaudado = venta_realizada + total_recaudado
        contador_ventas_diarias = contador_ventas_diarias + 1
    except Exception as error_valor_ingresado:
        print(f"ERROR DE VALOR INGRESADO!! {error_valor_ingresado}")
print(f"Ventas diarias realizadas : {contador_ventas_diarias} y el total recaudado : {total_recaudado}")