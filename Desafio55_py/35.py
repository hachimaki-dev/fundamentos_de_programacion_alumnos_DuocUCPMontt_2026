trasferencia_dia = [15000 , 80000 , 2000 , 150000]
importantes = []

for t in trasferencia_dia:

    if t > 50000:
        print("ALTO PERFIL")
        importantes.append(t)

print(importantes)