GB_totales = 1024*16
Gigabyte = 1024
GB_en_uso = Gigabyte+200
uso_del_sistema = Gigabyte*2+500
uso_de_programas = GB_en_uso*4

ram_disponible = GB_totales - (uso_de_programas + uso_del_sistema)


print(f"La ram Disponible son {ram_disponible} MB")


