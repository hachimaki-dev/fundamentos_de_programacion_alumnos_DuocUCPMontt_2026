freq = {'buen': 0, 'mal': 0}
comentario = "buen servicio mal precio buen ambiente"
palabras = comentario.split()
for palabra in palabras:
    if palabra in freq:
        freq[palabra] += 1

print(freq)