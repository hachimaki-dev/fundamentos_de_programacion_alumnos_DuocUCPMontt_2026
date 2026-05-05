procesador = 250000
placa_madre = 120000
tarjeta_de_video = 450000
descuento = 15
tarjeta_de_video = tarjeta_de_video - tarjeta_de_video * descuento / 100
total_pago = tarjeta_de_video + procesador + placa_madre
print(f"el total a pagar es:{total_pago}")