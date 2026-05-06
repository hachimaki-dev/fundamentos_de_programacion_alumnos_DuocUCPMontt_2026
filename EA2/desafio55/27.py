'''Ejercicio 27: Saltar Errores del Sistema (Kiosko)
El sistema del almacén falló y guardó ventas negativas. Debes limpiar la caja.

Datos Iniciales: Las ventas del día son: `[1500, -200, 5000, 0, 100]`. Tienes una variable total en 0.

Reglas de Negocio: Evidentemente, una venta no puede ser menor o igual a 0. Esos son errores del sistema. Necesitas sumar todas las ventas buenas y simplemente IGNORAR las malas, sin detener el ciclo.

Restricciones: Adentro de tu `for`, pon un `if` que detecte las ventas falsas y use la palabra mágica `continue` para saltárselas y pasar directo al siguiente número. Imprime la suma total limpia al final.'''


ventas = [1500, -200, 5000, 0, 100]
total = 0

for venta in ventas:
    if venta <= 0:
        continue
    else:
        total += venta
print(f"total: {total}")