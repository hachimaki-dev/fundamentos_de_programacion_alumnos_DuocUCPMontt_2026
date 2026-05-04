gb_servidor = 16
GB_SO = 2.5
gb_programas = 1.2*4

gasto_gb_total = gb_programas + GB_SO
gb_restante = gb_servidor - gasto_gb_total

ram_restante = gb_restante * 1024 #Megabytes

print(ram_restante)