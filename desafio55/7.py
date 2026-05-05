procesador= 250000
placa_madre= 120000
tarjeta_video= 450000
descuento_tarjeta_video = 15
precio_final_video = tarjeta_video - (tarjeta_video * descuento_tarjeta_video)/100

print(precio_final_video)
precio_final= (procesador + placa_madre + precio_final_video)
print(precio_final)
