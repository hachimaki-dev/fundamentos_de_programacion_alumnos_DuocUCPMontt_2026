gb = 1024
ram_servidor = 16
sistema_operativo = 2.5
uso_ram_programa = 1.2
programas_en_uso = 4
uso_ram_total = sistema_operativo + programas_en_uso * uso_ram_programa
ram_libre = ram_servidor - uso_ram_total
print(ram_libre * gb)