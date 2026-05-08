transferencias = [15000, 80000, 2000, 150000]
lista_blanca = []

for transferencia in transferencias:
    if transferencia > 50000:
        lista_blanca.append(transferencia)
        
print(lista_blanca)
        
        