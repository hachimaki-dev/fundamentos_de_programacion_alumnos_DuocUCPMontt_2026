ram_total_server = 16 #GB
consumo_ram_sistema = 2.5
consumo_ram_programas = (1.2 * 4)
ram_libre_GB = ram_total_server - (consumo_ram_sistema + consumo_ram_programas)
ram_libre_MB = ram_libre_GB * 1024
print(f"RAM libre: {ram_libre_MB} MB")