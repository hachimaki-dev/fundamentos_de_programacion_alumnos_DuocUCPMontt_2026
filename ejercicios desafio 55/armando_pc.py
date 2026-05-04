valor_procesador = 250000
valor_placa_madre = 120000
valor_tarjeta_video = 450000
descuento_especial = valor_tarjeta_video*0.15
total_final = valor_procesador + valor_placa_madre + (valor_tarjeta_video - descuento_especial)
print(f"tu total es de {total_final}")