texto = 'buen servicio mal precio buen ambiente'
freq = {'buen': 0, 'mal': 0}
palabras = texto.split()
for palabra in palabras:
    if palabra in freq:
        freq[palabra] = freq[palabra] + 1
print(freq)