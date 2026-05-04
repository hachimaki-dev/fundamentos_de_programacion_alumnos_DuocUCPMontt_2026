# Ejercicio 16: Contador de votos
# Define la lista votos = ['A', 'A', 'B', 'C', 'A', 'B']. Crea un diccionario vacío llamado resultados. 
# Recorre la lista y cuenta cuántas veces aparece cada letra. Guarda ese conteo en el diccionario e imprime el resultado final.

votos = ['A', 'A', 'B', 'C', 'A', 'B']
resultados = {}

resultados["votosA"] = 0
resultados["votosB"] = 0
resultados["votosC"] = 0

for voto in votos:
    if voto == "A":
        resultados["votosA"] += 1
    elif voto == "B":
        resultados["votosB"] += 1
    elif voto == "C":
        resultados["votosC"] += 1

print(resultados)
