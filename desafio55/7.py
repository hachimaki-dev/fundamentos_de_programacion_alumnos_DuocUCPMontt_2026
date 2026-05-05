#Ejercicio 7: Armando el PC Gamer

valor_procesador = 250000
valor_placamadre = 120000
valor_tarjeta = 450000
descuento_tarjeta = 15


tarjeta = (valor_tarjeta * descuento_tarjeta) / 100
total_descuento = valor_tarjeta - tarjeta
precio_total = valor_procesador + valor_placamadre + total_descuento

print(precio_total)

