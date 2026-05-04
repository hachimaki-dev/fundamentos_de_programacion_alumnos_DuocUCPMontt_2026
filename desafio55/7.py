"""
Ejercicio 7: Armando el PC Gamer
Estás armando tu PC y la tienda te dio un descuento especial en una de las piezas.

Datos Iniciales: Vas a comprar un procesador (250000), una placa madre (120000) y una tarjeta de video (450000).

Reglas de Negocio: Tienes un descuento del 15% SÓLO en la tarjeta de video. Las otras piezas mantienen su precio normal.

Restricciones: Asegúrate de restarle el descuento a la tarjeta de video antes de sumar el total final. Imprime el precio total de tu compra.

"""

valor_procesador = 250000 # 250,000
valor_placa_madre = 120000 # 120,000
valor_tarjeta_de_video = 450000 # 450,000

#DESCUENTO
descuento = 0,15
descuento_tarjeta_de_video = valor_tarjeta_de_video * 0.15

valor_total = valor_procesador + valor_placa_madre + valor_tarjeta_de_video - descuento_tarjeta_de_video
print(valor_total)