servidor = 16384
sistema_operativo = 2560
programas = 1228.8

total_ocupado = sistema_operativo + (programas * 4)

disponible = servidor - total_ocupado

print(f"El total de Ram disponible actualmente\n:{disponible}mb")