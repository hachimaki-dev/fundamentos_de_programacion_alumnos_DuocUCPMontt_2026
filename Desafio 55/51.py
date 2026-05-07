comentario_cliente = "buen servicio mal precio buen ambiente"

freq = {"buen" : 0,
        "mal" : 0}

comentario_cliente_como_lista = comentario_cliente.split()

for palabra in comentario_cliente_como_lista :
    if palabra in freq :
        if palabra == "buen" :
            freq["buen"] += 1
        if palabra == "mal" :
            freq["mal"] += 1

print(freq)