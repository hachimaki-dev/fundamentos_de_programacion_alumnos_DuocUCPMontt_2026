servidor_1 = ['U1', 'U2']
servidor_2 = ['U2', 'U3']
for usuario in servidor_2:
    if usuario not in servidor_1:
        servidor_1.append(usuario)
print(servidor_1)