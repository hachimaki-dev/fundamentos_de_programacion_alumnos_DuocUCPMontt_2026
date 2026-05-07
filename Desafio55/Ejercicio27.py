"""Ejercicio 27: Saltar Errores del Sistema (Kiosko)
El sistema del almacén falló y guardó ventas negativas. Debes limpiar la caja.

Datos Iniciales: Las ventas del día son: `[1500, -200, 5000, 0, 100]`. Tienes una variable total en 0.

Reglas de Negocio: Evidentemente, una venta no puede ser menor o igual a 0. 

Esos son errores del sistema. Necesitas sumar todas las ventas buenas y simplemente IGNORAR las malas, sin detener el ciclo.

Restricciones: Adentro de tu `for`, pon un `if` que detecte las ventas falsas y use la palabra mágica `continue` 
para saltárselas y pasar directo al siguiente número. Imprime la suma total limpia al final."""

Ventas_del_Dia = [1500, -200, -5000, 0, 100, 3400, -8349, -232, 2, 333, 32423, -4343421]

Cuenta_Total = 0

for cada_venta_del_dia in Ventas_del_Dia:
    if cada_venta_del_dia < 0:
        continue
    Cuenta_Total += cada_venta_del_dia

print(f"Recaudaste {Cuenta_Total}")
