#servidor tiene 16 GB en total
#El sistema operativo siempre usa 2.5 GB.
#Tienes 4 programas corriendo y cada uno usa 1.2 GB. (Recuerda que 1 GB son 1024 MB).

ram_total = 16
sistema_operativo = 2.5
programas_corriendo = 4
consumo_programa = 1.2

print("Consume en total: ")
print((ram_total - (sistema_operativo + (programas_corriendo * consumo_programa))) * 1024)