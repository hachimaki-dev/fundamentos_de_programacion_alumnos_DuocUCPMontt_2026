#Define la lista votos = ['A', 'A', 'B', 'C', 'A', 'B']. Crea un diccionario vacío llamado resultados. 
#Recorre la lista y cuenta cuántas veces aparece cada letra. Guarda ese conteo en el diccionario e imprime el resultado final.
votos = ['A', 'A', 'B', 'C', 'A', 'B']
resultados = {}
for voto in votos:
    if voto in resultados:
        resultados[voto] += 1
    else:
        resultados[voto] = 1

print(resultados)