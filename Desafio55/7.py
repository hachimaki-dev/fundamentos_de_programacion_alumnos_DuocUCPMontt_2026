procesador = 250000
placa_madre = 120000
tarjeta_de_video = 450000
descuento =  (tarjeta_de_video * 15) / 100
tarjeta_de_video = tarjeta_de_video - descuento
precio_final = procesador + placa_madre + tarjeta_de_video
print(precio_final)