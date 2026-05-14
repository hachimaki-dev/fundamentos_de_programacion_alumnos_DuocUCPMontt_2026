texto = "buen servicio mal precio buen ambiente"
freq = {"buen": 0, "mal": 0}

for palabra in texto.split():
    if palabra in freq:
        freq[palabra] += 1

print(freq)