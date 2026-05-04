total_ram_en_server = 16 # GB
uso_ram_idle = 2.5
uso_ram_por_programa = 1.2

uso_ram_en_gb = uso_ram_idle + (uso_ram_por_programa * 4) # 4 programas a la vez

ram_restante_en_gb = total_ram_en_server - uso_ram_en_gb
ram_restante_en_mb = ram_restante_en_gb * 1024
print(ram_restante_en_mb)
