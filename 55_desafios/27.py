#El sistema del almacén falló y guardó ventas negativas. Debes limpiar la caja.

ventas_día = [1500, -200, 5000, 0, 100]
total = 0

#Reglas de Negocio: Evidentemente, una venta no puede ser menor o igual a 0. Esos son errores del sistema. Necesitas sumar todas las ventas buenas y simplemente IGNORAR las malas, sin detener el ciclo.

#Restricciones: Adentro de tu `for`, pon un `if` que detecte las ventas falsas y use la palabra mágica `continue` para saltárselas y pasar directo al siguiente número. Imprime la suma total limpia al final.

for i in ventas_día:
    if i <= 0:
        continue
    elif i > 0:
        total += i

print({total})