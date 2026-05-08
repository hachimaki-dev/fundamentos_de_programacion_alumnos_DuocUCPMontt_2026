comentario_c = 'buen servicio mal precio buen ambiente'
freq = {'buen': 0, 'mal': 0}
lista_de_palabras = comentario_c.split()


for i in lista_de_palabras:
    if i == "buen":
        freq["buen"] += 1
    elif i == "mal":
        freq["mal"] += 1
    
print(freq)
