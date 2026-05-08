freq = {'buen': 0, 'mal': 0}
opinion = ("buen servicio mal precio buen ambiente")
palabras = opinion.split()
for i in palabras:
    if i in freq:
        freq[i] += 1
print(freq)