procesador = 250000
placa_madre = 120000
tarjeta_video = 450000
descuento = 0.15

descuento_tarjeta_video = tarjeta_video * descuento
precio_tarjeta_con_descuento = tarjeta_video - descuento_tarjeta_video

precio_total = procesador + placa_madre + precio_tarjeta_con_descuento

print(f"el precio con tu descuento es de {precio_total}")
