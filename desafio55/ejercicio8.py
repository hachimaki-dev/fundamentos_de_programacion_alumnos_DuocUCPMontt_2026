gb_totales_servidor = 16
gb_sistema_operativo = 2.5
gb_programas = 1.2
programas_andando = 4
gb_programas_totales = gb_programas * programas_andando
gb_sistema_programas = gb_programas_totales + gb_sistema_operativo
gb_libres = gb_totales_servidor - gb_sistema_programas
gb_libres_mb = gb_libres * 1024
print(gb_libres_mb)
