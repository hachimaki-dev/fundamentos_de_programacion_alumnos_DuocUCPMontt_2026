comentario_cliente = "buen servicio mal precio pero buen ambiente" #si lo pongo con una mayuscula ya no sirve bien y en vez de mostrar 2 buen muestra 1

freq = {"buen": 0, "mal": 0}

palabra = comentario_cliente.split()

for reseña in palabra:
    if reseña in freq:
        freq[reseña] += 1

print(freq)