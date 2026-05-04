precio_cpu = 250000
precio_motherboard = 120000
precio_gpu = 450000
porcentaje_descuento_en_gpu = 15

precio_gpu_descontado = precio_gpu - (precio_gpu / 100 * porcentaje_descuento_en_gpu)

total = precio_cpu + precio_motherboard + precio_gpu_descontado

print(total)
