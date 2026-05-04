#Estás armando tu PC y la tienda te dio un descuento especial en una de las piezas.
#Datos Iniciales: Vas a comprar un procesador (250000), una placa madre (120000) y una tarjeta de video (450000).
#Reglas de Negocio: Tienes un descuento del 15% SÓLO en la tarjeta de video. Las otras piezas mantienen su precio normal.
#Restricciones: Asegúrate de restarle el descuento a la tarjeta de video antes de sumar el total final. Imprime el precio total de tu compra.
precio_procesador = 250000
precio_placamadre = 120000
precio_tarjetavideo = 450000
descuento_tarjetaV = 0.15
descuento = precio_tarjetavideo * descuento_tarjetaV
precio_tarjetaV_descontado = precio_tarjetavideo - descuento
total = precio_tarjetaV_descontado + precio_placamadre + precio_procesador
print(total)