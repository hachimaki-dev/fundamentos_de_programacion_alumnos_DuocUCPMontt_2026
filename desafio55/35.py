transferencias_del_dia = [ 15000, 80000, 2000, 150000 ]
importantes = []
minimo_alto_perfil = 50000

for i in transferencias_del_dia:
    if i > minimo_alto_perfil:
        importantes.append(i)
    else:
        pass

print(importantes)
