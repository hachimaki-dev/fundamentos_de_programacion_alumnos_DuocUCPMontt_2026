gb_servidor = 16
gb_sistema_operativo = 2.5
cantidad_de_programas_corriendo = 4
gb_por_programa = 1.2
gb_a_mb = 1024

gasto_total_en_gb = gb_sistema_operativo + (gb_por_programa * cantidad_de_programas_corriendo)
espacio_libre_en_gb = gb_servidor - gasto_total_en_gb
espacio_libre_en_mb = espacio_libre_en_gb * gb_a_mb

print(espacio_libre_en_mb)