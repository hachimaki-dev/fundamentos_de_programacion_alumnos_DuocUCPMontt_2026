lista_de_codigos = [200, 404, 500, 200, 500]
reintento = 1

for codigo in lista_de_codigos:
    if codigo == 200:
        print("OK")
    elif codigo == 404:
        print("no encontrado")
    elif codigo == 500:
        reintento = reintento - 1

        if reintento < 0:
            print("servidor caidos")
            break
        else:
            print("reintentado")
