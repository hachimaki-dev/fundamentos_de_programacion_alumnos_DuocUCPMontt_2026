procesador = 250000
placa_madre = 120000
tarjeta_video = 450000

descuento = tarjeta_video * 0.15
total_final = procesador + placa_madre + (tarjeta_video - descuento)

print(f"Total final: ${total_final}")