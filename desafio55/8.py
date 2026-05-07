ram = 16
ram_mb = 1024
sistema = 2.5
por_programa = 1.2
restante = ram - (sistema + por_programa * 4)
print(restante * ram_mb)