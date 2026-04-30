votos = ["A", "A", "B", "C", "A", "B"]

resultados = {}

contador_a = 0
contador_b = 0
contador_c = 0

for voto in votos :
    if voto == "A" :
        contador_a += 1
    if voto == "B" :
        contador_b += 1
    if voto == "C" :
        contador_c += 1

resultados.update({"A" : contador_a, "B" : contador_b, "C" : contador_c})

print(resultados)