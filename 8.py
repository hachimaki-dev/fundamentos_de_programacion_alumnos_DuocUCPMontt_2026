valor_gb = 1024 
ram_total = 16 
gb_sistema_operativo = 2.5
programas_corriendo = 4
gb_de_cada_programa = 1.2

uso_de_programas = programas_corriendo * gb_de_cada_programa
uso_total = gb_sistema_operativo + uso_de_programas

ram_libre = ram_total - uso_total
conversion_al_mb = ram_libre * valor_gb

print(conversion_al_mb)




