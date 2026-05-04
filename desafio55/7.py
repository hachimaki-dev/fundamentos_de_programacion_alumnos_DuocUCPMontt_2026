procesador = 250000
placa_madre = 120000
tarjeta_video = 450000
descuento_tarjeta_video = tarjeta_video * 0.15
nuevo_precio = tarjeta_video - descuento_tarjeta_video 
total_compra = procesador + placa_madre + nuevo_precio
print(f"El total de tu compra es de {total_compra} pesos.")