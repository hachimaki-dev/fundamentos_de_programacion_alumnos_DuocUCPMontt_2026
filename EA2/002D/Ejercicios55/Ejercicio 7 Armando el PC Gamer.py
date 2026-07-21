# Ejercicio 7: Armando el PC Gamer
# Estás armando tu PC y la tienda te dio un descuento especial en una de las piezas.

# Datos Iniciales: Vas a comprar un procesador (250000), una placa madre (120000) y una tarjeta de video (450000).

# Reglas de Negocio: Tienes un descuento del 15% SÓLO en la tarjeta de video. Las otras piezas mantienen su precio normal.

# Restricciones: Asegúrate de restarle el descuento a la tarjeta de video antes de sumar el total final. Imprime el precio total de tu compra.

procedador = 250000
placa_madre = 120000
tajeta_de_video = 450000
descuento = 0.15

descuento_total = tajeta_de_video * descuento
tajeta_de_video = tajeta_de_video - descuento_total

suma_total = procedador + placa_madre + tajeta_de_video

print(suma_total)