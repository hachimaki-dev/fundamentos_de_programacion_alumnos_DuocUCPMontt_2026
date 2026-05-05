giga = 1024
ram_servidor =  16
sistema_operativo = 2.5
programa = 1.2

total_giga = sistema_operativo + (programa * 4)

total_megas = (ram_servidor - total_giga) * giga
print(total_megas)