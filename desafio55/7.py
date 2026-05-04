procesador = 250000
placa_madre = 120000
tarjeta_video = 450000
descuento_video = tarjeta_video/100*15
tarjeta_video_d = tarjeta_video - descuento_video
precio_final = procesador + placa_madre + tarjeta_video_d
print(precio_final)