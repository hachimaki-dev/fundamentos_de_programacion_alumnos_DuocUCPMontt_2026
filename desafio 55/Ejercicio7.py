procesador = 250000
placa_madre = 120000
tarjeta_grafica = 450000
total_a_pagar = (tarjeta_grafica * 0.85) + placa_madre + procesador
print(f"Me voy a comprar un procesador, una placa madre y una tarjeta grafica")
print(f"El procesador sale ${procesador}CLP")
print(f"La placa madre sale ${placa_madre}CLP")
print(f"Y la tarjeta grafica cuesta ${tarjeta_grafica}CLP, PERO para tu suerte tiene un 15% de descuento")
print(f"El precio final de la grafica es de ${tarjeta_grafica * 0.85}CLP")
print(f"El total seria de ${procesador + placa_madre + tarjeta_grafica}CLP, pero con el descuento queda en ${total_a_pagar}CLP")