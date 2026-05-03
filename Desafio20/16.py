votos = ["A","A","B","C","A","B"]
resultados = {}
for voto in votos:
    if voto in resultados:
        resultados[voto] += 1
    else:
        resultados[voto] = 1
print(resultados)