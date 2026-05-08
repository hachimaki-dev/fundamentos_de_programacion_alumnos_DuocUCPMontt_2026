comentario = input("Ingresa un comentario: ")
freq = {'buen': 0, 'mal': 0}
 
palabras = comentario.split()
 
for palabra in palabras:
    if palabra in freq:
        freq[palabra] += 1
 
print(freq)