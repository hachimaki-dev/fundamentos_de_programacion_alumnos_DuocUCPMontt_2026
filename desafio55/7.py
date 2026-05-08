"""
Ejercicio 7: Armando el PC Gamer
Estás armando tu PC y la tienda te dio un descuento especial en una de las piezas.

Datos Iniciales: Vas a comprar un procesador (250000), una placa madre (120000) y una 
tarjeta de video (450000).

Reglas de Negocio: Tienes un descuento del 15% SÓLO en la tarjeta de video. Las otras 
piezas mantienen su precio normal.

Restricciones: Asegúrate de restarle el descuento a la tarjeta de video antes de sumar 
el total final. Imprime el precio total de tu compra.

Resultado esperado en consola:
752500.0
"""

procesador = 250000
placa_madre = 120000
tarj_video = 450000

multiplico = tarj_video * 0.15
descuento = tarj_video - multiplico
total = procesador + placa_madre + descuento

print(f"El precio total de la compra con el 15% de descuento aplicado es de: ${total}")