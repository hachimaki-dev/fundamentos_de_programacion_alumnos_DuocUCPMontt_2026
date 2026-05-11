# Ejercicio 51: Análisis de Sentimiento Básico (Twitter)

print("==================================")
print("Sistema de análisis de comentarios")
print("==================================")

comentario = 'buen servicio mal precio buen ambiente'

freq = {'buen': 0, 'mal': 0}

palabras = comentario.split()

for palabra in palabras:
    if palabra in freq:
        freq[palabra] = freq[palabra] + 1

print(freq)