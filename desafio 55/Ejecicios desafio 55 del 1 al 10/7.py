procesador = 250000
placa_madre = 120000
GPU = 450000

descuento_gpu = (GPU * 0.15)
valor_gpu = (GPU - descuento_gpu)

total_a_pagar = (procesador + placa_madre + valor_gpu)

print("Vas a comprarte unas piezas para el armado de tu PC GAMER, cada pieza te cuesta lo siguiente:")
print(" Procesador: 250000.")
print(" Placa Madre: 120000.")
print(" Trajeta de video: 450000.")

input()

print("Por ser un nuevo cliente, la tienda te dio un 15% de descuento que aplica unicamente para el valor de la Tarjeta Grafica.")

input()

print(f"El total de las piezas con el 15% de descuento en la tajeta Grafica queda en: {total_a_pagar}")

