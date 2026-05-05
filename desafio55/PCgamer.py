#  Vas a comprar un procesador (250000), una placa madre (120000) y una tarjeta de video (450000).
# Tienes un descuento del 15% SÓLO en la tarjeta de video. Las otras piezas mantienen su precio normal.
# Datos Iniciales
procesador = 250000
placa_madre = 120000
tarjeta_video = 450000
descuento_tarjeta_video = tarjeta_video * 0.15
precio_final_tarjeta = tarjeta_video - descuento_tarjeta_video
print(f"te haz comprado un procesaor de {procesador} mil pesos , una placa madre de {placa_madre} mil pesos y una tarjeta de video de {tarjeta_video} mil pesos PERO tienes un descuento del 15% en la tarjeda de video que te lo deja en {precio_final_tarjeta} ")
precio_final_total = procesador + placa_madre + precio_final_tarjeta
print(f" el precio final es de {precio_final_total}")




