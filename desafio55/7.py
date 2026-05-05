valor_procesador = 250000
valor_placa_madre = 120000
valor_tarjeta_video = 450000

descuento_tarjeta_video = (valor_tarjeta_video * 15) / 100

valor_final_tarjeta = valor_tarjeta_video - descuento_tarjeta_video

valor_total = valor_procesador + valor_placa_madre + valor_final_tarjeta

print(f"Tiene un costo total de {valor_total}")