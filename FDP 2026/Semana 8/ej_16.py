# Tienes una lista llamada votos.

# Debes crear un diccionario llamado resultados que cuente cuántas veces aparece cada opción.

votos = ["A","B","B","B","B","A","A","A","A","A"]

resultados = {"A": 0, "B": 0}

for voto in votos:
    if voto == "A":
        resultados.update({"A": resultados.get("A") + 1})
    else:
        resultados.update({"B": resultados.get("B") + 1})

print(resultados)