RAM_a_mb = 1024
RAM_server = 16
RAM_SO = 2.5
cantidad_de_ram_x_programa = 1.2
RAM_gastada = RAM_SO + (cantidad_de_ram_x_programa*4)
RAM_Libre = RAM_server - RAM_gastada
Mb_disponibles = RAM_Libre * RAM_a_mb
print(f"Quedan {Mb_disponibles} Megabytes disponibles.")