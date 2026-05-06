#Ejercicio 7: Armando el PC Gamer
#Estás armando tu PC y la tienda te dio un descuento especial en una de las piezas.

#Datos Iniciales: Vas a comprar un procesador (250.000), una placa madre (120.000) y una tarjeta de video (450.000).

#Reglas de Negocio: Tienes un descuento del 15% SÓLO en la tarjeta de video.
#Las otras piezas mantienen su precio normal.

#Restricciones: Asegúrate de restarle el descuento a la tarjeta de video antes de sumar el total final.
#Imprime el precio total de tu compra.

procesador=250000
placa_madre=120000
tarjeta_video=450000

tarjeta_descuento=tarjeta_video*0.85
armado_pc=procesador+placa_madre+tarjeta_descuento
print(armado_pc)