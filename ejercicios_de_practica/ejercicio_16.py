votos = ["A", "B", "B", "C", "D", "A", "A"]

resultados = {}

for eleccion in votos:
    if eleccion in resultados:
        resultados[eleccion] += 1

    else:
        resultados[eleccion] = 1
        
print(resultados)