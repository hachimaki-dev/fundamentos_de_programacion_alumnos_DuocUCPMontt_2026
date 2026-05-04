gb_total = 16
gb_del_SO = 2.5
programas_gb = 1.2*4
gb_ocupado = gb_del_SO + programas_gb
gb_libres = gb_total - gb_ocupado
gb_libres = gb_libres * 1024
print(gb_libres)