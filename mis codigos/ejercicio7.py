procesador = 250000
placa_madre = 120000
gpu = 450000

print(f"Estos son los precios totales de los productos\n:{procesador + placa_madre + gpu} \n")

descuento = gpu * 0.15

precio_total_gpu = gpu - descuento

print(f"El costo total de los componentes mas el descuento es de \n:{precio_total_gpu + placa_madre + procesador}")