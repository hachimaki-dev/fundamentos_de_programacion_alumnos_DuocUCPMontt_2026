
comentario = "buen servicio mal precio buen ambiente"
freq = {"buen": 0,
        "mal": 0}
for i in comentario.split():
    if i == "buen":
        freq["buen"] += 1
    elif i == "mal":
        freq["mal"] += 1
print(freq)