votos = ['A', 'A', 'B', 'C', 'A', 'B']

resultados = {}


for voto in votos:
    
    resultados[voto] = resultados.get(voto, 0) + 1


print(resultados)
