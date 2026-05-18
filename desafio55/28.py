patentes = ["XY11", "ZZ99", "AB12", "XX00"]
patentes_buscada = "AB12"
for patente in patentes:
    print("Buscando en " + patente + "...")

    if patente == patentes_buscada:
        print("Sospechoso encontrado")
        break