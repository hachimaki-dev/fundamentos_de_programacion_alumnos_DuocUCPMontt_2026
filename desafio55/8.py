servidor_gb = 16
OS = 2.5
programas_corriendo = 4
gasto_programas = 1.2
suma = OS + programas_corriendo * gasto_programas
ram_restante = servidor_gb - suma
ram_restante = ram_restante * 1024
print(ram_restante)

