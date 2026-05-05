precio_procesador = 250000
precio_placa_madre = 120000
precio_tarjeta_de_video = 450000

descuento_tarjeta_video = precio_tarjeta_de_video * 0.15
precio_video_final = precio_tarjeta_de_video - descuento_tarjeta_video
total_compra = precio_video_final + precio_procesador + precio_placa_madre

print("DETALLES DE TU COMPRA")
print(f"procesador: ${precio_procesador}")
print(f"placa madre: ${precio_placa_madre}")
print(f"tarjeta de video: $ {precio_video_final} INCLUYE UN 15% DE DESCUENTO")
print("-----------------")
print(f"TOTAL A PAGAR: {total_compra}")