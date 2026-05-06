memoria_del_servidor = 16
sistema_operativo = 2.5
programas = 1.2

memoria_disponible = (memoria_del_servidor - sistema_operativo - (programas * 4)) * 1024
print(memoria_disponible)