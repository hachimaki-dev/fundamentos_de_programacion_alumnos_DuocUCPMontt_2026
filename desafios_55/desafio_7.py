procesador = 250000
placa_madre = 120000
tarjeta_de_video = 450000

descuento_tarjeta = tarjeta_de_video * 0.15
precio_gpu = tarjeta_de_video - descuento_tarjeta

total_final = (procesador + placa_madre + precio_gpu)

print(f"Precio total de la compra: ${total_final}")