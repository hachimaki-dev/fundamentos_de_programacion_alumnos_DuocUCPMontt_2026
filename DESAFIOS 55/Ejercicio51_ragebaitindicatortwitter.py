comentario= 'buen servicio mal precio buen ambiente'
freq = {'buen': 0, 'mal': 0}


for i in comentario.split():
    if i in freq:
        freq[i] += 1
print(freq)        