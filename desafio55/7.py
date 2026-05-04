precio_procesador = 250000
precio_placa_madre = 120000
precio_tarjeta_de_video = 450000

descuento = precio_tarjeta_de_video*15/100
total_tarjeta = (precio_tarjeta_de_video - descuento)
total = (precio_placa_madre + precio_procesador + total_tarjeta)

print(f"El precio total MÁS el descuento de la tarjea de video da en total {total}")
