total_ram_gb = 16
sistema_operativo_gb = 2.5
programas_cantidad = 4
consumo_por_programa_gb = 1.2

consumo_programas_total = programas_cantidad * consumo_por_programa_gb

ram_libre_gb = total_ram_gb - sistema_operativo_gb - consumo_programas_total

ram_libre_mb = ram_libre_gb * 1024

print(ram_libre_mb)