comentario = 'buen servicio mal precio buen ambiente'
    
freq ={"buen": 0, "mal": 0}
palabras = comentario.split()


for palabras in palabras:
    if palabras in freq:
        freq[palabras] +=1
print(freq)
        
    