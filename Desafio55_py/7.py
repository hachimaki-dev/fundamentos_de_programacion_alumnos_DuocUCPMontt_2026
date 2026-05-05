procesador = 250000
placa_madre = 120000
tarjeta_video = 450000

descuento = tarjeta_video * 0.15
descuento = tarjeta_video - descuento 

compra = procesador + placa_madre + descuento


print(f"El precio de su compra es {compra}")
