patentes = ["XY11", "ZZ99", "AB12", "XX00"]
robado = "AB12"

for patentes in patentes:
    print("buscando en", patentes + "...")
    if patentes == robado:
        print("sospechoso encontrado")
        break
    