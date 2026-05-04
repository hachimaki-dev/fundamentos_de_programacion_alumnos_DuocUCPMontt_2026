procesador = 250000
placa_madre = 120000
tarjeta_video = 450000
descuento = 450000 * 0.15

tarjeta_con_descuento = tarjeta_video - descuento
total = procesador + placa_madre + tarjeta_con_descuento

print(f"total de los productos con el descuento es de: {total}")