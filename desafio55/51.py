comentario_client = "buen servicio mal precio buen ambiente"
freq = {"buen": 0, "mal": 0}
for palabra in comentario_client.split():
    if palabra == "buen":
        freq["buen"] += 1
    elif palabra == "mal":
        freq["mal"] += 1
print(freq)