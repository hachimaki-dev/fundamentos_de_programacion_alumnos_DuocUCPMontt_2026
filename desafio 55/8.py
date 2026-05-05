#total de gb servidor y mb servidor
total_ram_gb_servidor = 16
total_ram_mb_servidor = total_ram_gb_servidor * 1024

#la ram del SO en gb y en mb
ram_so_gb = 2.5
ram_so_mb = ram_so_gb * 1024


cantidad_gb_ram_programas_en_ejecucion = 4 * 1.2
cantidad_mg_ram_programas_en_ejecucion = 0
cantidad_gb_ram_programas_en_ejecucion * 1024 

total_ram_en_gb_disponibles = total_ram_gb_servidor - ram_so_gb - cantidad_gb_ram_programas_en_ejecucion

print(total_ram_en_gb_disponibles * 1024)