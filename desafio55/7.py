#Estás armando tu PC y la tienda te dio un descuento especial en una de las piezas.
#Datos Iniciales: Vas a comprar un procesador (250000), una placa madre (120000) y una tarjeta de video (450000).
#Reglas de Negocio: Tienes un descuento del 15% SÓLO en la tarjeta de video. Las otras piezas mantienen su precio normal.
#Restricciones: Asegúrate de restarle el descuento a la tarjeta de video antes de sumar el total final. Imprime el precio total de tu compra.
procesador = 250000
placa_madre = 120000
tarjeta_de_video = 450000
tarjeta_de_video_con_descuento = tarjeta_de_video * 0.15
tarjeta_de_video = tarjeta_de_video - tarjeta_de_video_con_descuento
pc_valor_total = procesador + placa_madre + tarjeta_de_video
print(pc_valor_total)
#752500.0