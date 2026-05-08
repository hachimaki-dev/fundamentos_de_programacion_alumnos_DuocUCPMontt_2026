transferencias_diarias = [15000 , 80000 , 2000 , 150000]
importante = []
for alto_perfil in transferencias_diarias:
    if alto_perfil > 50000:
        importante.append(alto_perfil)
print(importante)