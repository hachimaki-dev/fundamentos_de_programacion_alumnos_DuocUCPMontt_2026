"""Ejercicio 7: Armando el PC Gamer
Estás armando tu PC y la tienda te dio un descuento especial en una de las piezas.

Datos Iniciales: Vas a comprar un procesador (250000), una placa madre (120000) y una tarjeta de video (450000).

Reglas de Negocio: Tienes un descuento del 15% SÓLO en la tarjeta de video. Las otras piezas mantienen su precio normal.

Restricciones: Asegúrate de restarle el descuento a la tarjeta de video antes de sumar el total final. Imprime el precio total de tu compra."""


Procesador = 250000

Placa_Madre = 120000

Tarjeta_de_Video = 450000

Total_Pagar = Procesador + Placa_Madre + Tarjeta_de_Video * 0.85

print(Total_Pagar)