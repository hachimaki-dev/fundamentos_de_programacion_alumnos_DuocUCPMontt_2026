transferencias = [15000, 80000, 2000, 150000]
importantes = []
for trans in transferencias:
    if trans > 50000:
        print(f"{trans} es una transferencia de alto perfil, se abrira una investigación.")
        importantes.append(trans)
    else:
        print(f"{trans} es una transferencia normal, no se necesita investigación.")