votos = [ "A", "A", "B"]
contador_a = 0
contador_b = 0

for i in votos:
    if i == "A":
        contador_a = contador_a + 1
    else:
        contador_b = contador_b + 1

resultados = { "A": contador_a, "B": contador_b}
print(resultados)
