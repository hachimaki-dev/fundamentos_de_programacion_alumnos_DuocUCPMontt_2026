Servidor_1 = ["U1", "U2"]
Servidor_2 = ["U2", "U3"]

for usuario in Servidor_2:
    if usuario not in Servidor_1:
        Servidor_1.append(usuario)

print("Servidor 1 Final:", Servidor_1)