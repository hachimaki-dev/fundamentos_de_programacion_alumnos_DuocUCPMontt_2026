votos = ['A', 'A', 'B', 'C', 'A', 'B']
resultado = {}
for letra in votos:
    if letra in resultado:
        resultado[letra] += 1
    else:
        resultado[letra] = 1
print(resultado)