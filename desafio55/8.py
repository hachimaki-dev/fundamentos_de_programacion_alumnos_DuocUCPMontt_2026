servidor_gb_total = 16
sistema_operativo = 2.5
programas_corriendo = 4
uso_por_programa = 1.2
gasto_total = sistema_operativo + programas_corriendo * uso_por_programa
gasto_total = gasto_total * 1024
servidor_gb_total = servidor_gb_total * 1024
GB_libres = servidor_gb_total - gasto_total
print(GB_libres)