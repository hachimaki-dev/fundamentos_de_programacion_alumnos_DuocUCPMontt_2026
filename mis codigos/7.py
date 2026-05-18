procesador = 250000
placa_madre = 120000
tarjeta_video = 450000

descuento = tarjeta_video * 0.15

precio_final = procesador + placa_madre + (tarjeta_video - descuento)

print(f"el precio final de la pc es de {precio_final}")