total_ram_servidor = 16
sistema_operativo = 2.5
programas_corriendo = 4 * 1.2

gasto_sistema = sistema_operativo + programas_corriendo
total_gb_libres = total_ram_servidor - gasto_sistema
tranformacion_mb = total_gb_libres * 1024

print(f"La ram libre es de: {tranformacion_mb} MB")