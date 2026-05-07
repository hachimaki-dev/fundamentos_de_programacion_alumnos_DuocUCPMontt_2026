servidor_1 = ['U1', 'U2']
servidor_2 = ['U2', 'U3']

for servidor in servidor_2 :
    if servidor not in servidor_1 :
        servidor_1.append(servidor)

print(servidor_1)