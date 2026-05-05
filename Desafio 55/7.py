costo_procesador=250000
costo_placa_madre=120000
costo_tarjeta_video=450000

total_tarjeta_video=costo_tarjeta_video-(costo_tarjeta_video*15/100) #se le hizo un 15% dcto

total_compra=total_tarjeta_video+costo_placa_madre+costo_procesador

print(f"${total_compra} es el total de la compra")