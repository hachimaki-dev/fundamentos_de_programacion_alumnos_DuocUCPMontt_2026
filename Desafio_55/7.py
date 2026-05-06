GB_servidor = 16
Sistema_operativo_GB = 2.5
programas_corriendo_GB = 4.8

Gasto_sistema = Sistema_operativo_GB + programas_corriendo_GB

GB_libres = GB_servidor - Gasto_sistema

GB_final = GB_libres * 1024

print(GB_final)