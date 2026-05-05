# : El servidor tiene 16 GB en total. El sistema operativo siempre usa 2.5 GB. Tienes 4 programas corriendo y cada uno usa 1.2 GB. (Recuerda que 1 GB son 1024 MB).
# Suma lo que gasta el sistema y lo que gastan los programas. Réstale eso al total para saber cuántos GB quedan libres. Pero ojo, el resultado final debe estar en Megabytes (MB).


total_ram = 16
sistema_operativo = 2.5
programas = 1.2

print(f"El servidor tiene {total_ram} GB en total. El sistema operativo siempre usa {sistema_operativo} GB. Tienes 4 programas corriendo y cada uno usa {programas} GB.")
gastos_de_RAM = sistema_operativo + programas *4
gasto_total = total_ram - gastos_de_RAM
gasto_total = gasto_total * 1024
print(f"tienes de sobra {gasto_total} MB")



















