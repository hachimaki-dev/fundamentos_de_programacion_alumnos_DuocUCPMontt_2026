#Estás armando tu PC y la tienda te dio un descuento especial en una de las piezas.
#Datos Iniciales: Vas a comprar un procesador (250000), una placa madre (120000) y una tarjeta de video (450000).
#Reglas de Negocio: Tienes un descuento del 15% SÓLO en la tarjeta de video. Las otras piezas mantienen su precio normal.
#Restricciones: Asegúrate de restarle el descuento a la tarjeta de video antes de sumar el total final. Imprime el precio total de tu compra.
procesador = 250000
placa_madre = 120000
tarjeta_video = 450000
descuento = 0.15
monto1 = tarjeta_video * 0.15
tarjeta_video_descontada = tarjeta_video - monto1
total = placa_madre + procesador + tarjeta_video_descontada
print(f"el total a pagar es: {total}")