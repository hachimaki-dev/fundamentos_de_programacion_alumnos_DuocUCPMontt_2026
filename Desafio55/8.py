ram = 16
so = 2.5

consumo_x_programa = 1.2
cant_programas = 4

ram_restante_mb = (ram - (so + cant_programas * consumo_x_programa)) * 1024

print(ram_restante_mb)