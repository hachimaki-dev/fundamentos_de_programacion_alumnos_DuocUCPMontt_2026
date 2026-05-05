procesador = 250000
placa_madre = 120000
targeta_de_video = 450000
descuento = 0.15

precio_sin_desucento = procesador + placa_madre + targeta_de_video
precio_con_descuento = procesador + placa_madre + (targeta_de_video * (1 - descuento))

print(f"precio con descuento es {precio_con_descuento}")