precio_CPU = 250000
precio_motherboard = 120000
precio_GPU = 450000
porcentaje_descuento = 15
descuento = precio_GPU*porcentaje_descuento/100
precio_GPU = precio_GPU - descuento
precio_final = precio_CPU + precio_motherboard + precio_GPU
print(f"El total a pagar es de {precio_final}. ")