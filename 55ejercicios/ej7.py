# Resuelto Ejercicio 7: Armando el PC Gamer

print("------------------------------")
print("Calculadora de compra PC Gamer")
print("------------------------------")

procesador = 250000
placa_madre = 120000
tarjeta_video = 450000

descuento = tarjeta_video * 0.15

precio_tarjeta_descuento = tarjeta_video - descuento

total_compra = procesador + placa_madre + precio_tarjeta_descuento

print(total_compra)