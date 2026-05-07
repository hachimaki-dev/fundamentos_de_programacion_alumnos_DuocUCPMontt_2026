comentario = "buen servicio mal precio buen ambiente"
freq = {"buen": 0, "mal": 0}

legos = comentario.split()
for i in legos:
    if i == "buen":
        freq["buen"] += 1
    if i == "mal":
        freq["mal"] += 1

print(freq)