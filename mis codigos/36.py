servidor_uno = ["U1", "U2"]

servidor_dos = ["U2", "U3"]

for usuario in servidor_dos:

    if usuario not in servidor_uno:
        servidor_uno.append(usuario)

print("Servidor uno actualizado:", servidor_uno)