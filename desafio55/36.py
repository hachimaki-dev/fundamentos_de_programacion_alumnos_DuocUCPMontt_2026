servidor_1 = ['U1', 'U2']
servidor_2 = ['U2', 'U3']
contador = 0
for i in servidor_2:
    if i not in servidor_1:
        servidor_1.append(servidor_2[contador])
    contador += 1
print(servidor_1)
