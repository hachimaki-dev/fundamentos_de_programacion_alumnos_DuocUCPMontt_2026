comentario = "buen servicio mal precio buen ambiente"
comentario_splitted = comentario.split(" ")

freq = {'buen': 0, 'mal': 0}

for palabra in comentario_splitted:
    if palabra in freq:
        freq[palabra] += 1

print(freq)