votos = ["A", "A", "B", "C", "A", "B"]
resultado = {}
for voto in votos:
    if voto in resultado:
        resultado[voto] += 1
    else:
        resultado[voto] = 1
print(resultado)