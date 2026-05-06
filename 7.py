valor_procesador = 250000
valor_placa_madre = 120000
valor_tarjeta_video = 450000

descuento_tarjeta_de_video =  valor_tarjeta_video - (valor_tarjeta_video * 0.15)

valor_total_de_piezas = (valor_procesador + valor_placa_madre + descuento_tarjeta_de_video)
print(valor_total_de_piezas)