RAM_server = 16
sistema_operativo = 2.5
uso_RAM_programa = 1.2
suma_procesos = sistema_operativo + (uso_RAM_programa * 4)
GB_libres = RAM_server - suma_procesos

print(f"Tienes un servidor con {RAM_server} GB de RAM, con la memoria que usa el SO y los procesos en ejecución actuales tienes disponible: {GB_libres} GB \nLo que se traduce en MB a: {GB_libres * 1024} MB.")