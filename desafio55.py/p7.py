valor_procesador = 250000
placa_madre = 120000
tarjeta_de_video = 450000

descuento = tarjeta_de_video // 100 * 15
tarjeta_descontada = tarjeta_de_video - descuento

valor_total = valor_procesador + placa_madre + tarjeta_descontada
print(valor_total)