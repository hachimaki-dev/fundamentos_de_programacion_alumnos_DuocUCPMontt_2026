servidor = 16
sistema_operativo = 2.5
programas = 1.2

cantidad_de_programas = programas * 4

gasto_de_restante = sistema_operativo + cantidad_de_programas

ram_libre = servidor - gasto_de_restante

total_en_megabytes = ram_libre * 1024
print(total_en_megabytes)