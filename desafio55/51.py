freq = {'buen': 0, 'mal': 0}
comentario =  'buen servicio mal precio buen ambiente'
for i in comentario.split():
    if i in freq:
        freq[i] +=1


print(freq)