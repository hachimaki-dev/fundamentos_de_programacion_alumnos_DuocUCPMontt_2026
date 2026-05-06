transferencias_del_dia = [15000,80000,2000,150000]
alto_perfil = []
for i in transferencias_del_dia:
    if i > 50000:
        alto_perfil.append(i)
print(alto_perfil)
