comentario_cliente = "buen servicio mal precio buen ambiente"

freq = {
    'buen' : 0,
    'mal' : 0
}
comentario_seccionado = comentario_cliente.split()

for elem in comentario_seccionado:
    if elem == 'buen':
        freq['buen'] += 1
    elif elem == 'mal':
        freq['mal'] += 1
print(freq)