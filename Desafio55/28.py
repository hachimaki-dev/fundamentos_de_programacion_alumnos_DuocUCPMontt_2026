patentes_que_pasaron=["XY11", "ZZ99", "AB12", "XX00"]
policia_busca="AB12"
for n in patentes_que_pasaron:
    if n !=policia_busca:
        print(f"Buscando en {n}")
    else:
        print(f"Buscando en {n}")
        print("Sospechoso encontrado")
        break