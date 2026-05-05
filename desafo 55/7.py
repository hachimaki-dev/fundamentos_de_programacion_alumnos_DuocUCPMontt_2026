procesador = 250000
placa_madre = 120000
tarjeta_de_video = 450000
descuento = 15

total_descuento = (tarjeta_de_video * descuento) / 100


tarjeta_de_video_con_descuento = tarjeta_de_video - total_descuento

total_compra = (procesador + placa_madre + tarjeta_de_video_con_descuento)
print(total_compra)