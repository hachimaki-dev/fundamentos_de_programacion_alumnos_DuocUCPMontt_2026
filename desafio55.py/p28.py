patentes = ["XY11", "ZZ99", "AB12", "XX00"]
patente_buscada= "AB12"

for patente in patentes:
    print("Buscando en", patente)
    if patente == patente_buscada:
        print("Sospechoso encontrado")
        break