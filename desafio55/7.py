procesador = 250000
placa_madre = 120000
tarjeta_de_video = 450000

descuento = tarjeta_de_video * 0.15
tarjeta_de_video_final = tarjeta_de_video - descuento
total_final = tarjeta_de_video_final + placa_madre + procesador
print(total_final)