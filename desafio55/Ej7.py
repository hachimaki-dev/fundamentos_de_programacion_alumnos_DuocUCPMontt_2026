#Ejercicio 7: Armando el PC Gamer
#Estás armando tu PC y la tienda te dio un descuento especial en una de las piezas.

#Datos Iniciales: Vas a comprar un procesador (250000), una placa madre (120000) y una tarjeta de video (450000).

#Reglas de Negocio: Tienes un descuento del 15% SÓLO en la tarjeta de video. Las otras piezas mantienen su precio normal.

#Restricciones: Asegúrate de restarle el descuento a la tarjeta de video antes de sumar el total final. Imprime el precio total de tu compra.

precio_proce = 250000
precio_mother = 120000
precio_grafica = 450000 - 450000 * 0.15

print("Tu precio total a pagar tras el SUPER HYPER MEGA DESCUENTO en la tarjeta gráfica es de: $", precio_proce + precio_mother + precio_grafica ," pesos.")


