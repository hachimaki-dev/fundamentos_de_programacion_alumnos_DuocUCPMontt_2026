total_servidor = 16
sistema_ocupa = 2.5
programas = 4.8

total_consumo_programas_y_sistema = (sistema_ocupa + programas)

ram_restante = (total_servidor - total_consumo_programas_y_sistema)

ram_restante_en_mb = (ram_restante * 1024)



print("Estás revisando cuánta memoria RAM le queda libre a tu servidor.")

print(f"El sistema consume: {sistema_ocupa} en GB y los Programas abiertos consumen: {programas} en GB.")

input()

print(f"La RAM restante del sistema es de {ram_restante_en_mb} en Megabytes.")