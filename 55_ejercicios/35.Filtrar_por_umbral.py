transferencias_del_dia = [15000, 80000, 2000, 150000]
lista_especial = []
for transferencia_especifica in transferencias_del_dia:
    if transferencia_especifica > 50000:
        lista_especial.append(transferencia_especifica)
print(lista_especial)