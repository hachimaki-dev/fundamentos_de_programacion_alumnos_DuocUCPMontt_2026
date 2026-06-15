def incrementar(numero):
    numero = numero + 1  # Esto crea un NUEVO número en memoria, no modifica el original

X = 5
incrementar(X)
print(X)  # Imprime 5, ¡no cambió!