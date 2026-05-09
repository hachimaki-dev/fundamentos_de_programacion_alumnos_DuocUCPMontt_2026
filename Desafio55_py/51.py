comentario = "buen servicio mal precio buen ambiente"
freq = {'buen': 0, 'mal': 0}

palabras  = comentario.split()

for i in palabras:

    if i in freq:
        freq[i] += 1


print(freq)