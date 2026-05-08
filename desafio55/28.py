patentes = ["XY11", "ZZ99", "AB12", "XX00"]
for sospechoso in patentes:
    if sospechoso != "AB12":
        print(f"buscando en {sospechoso}")
    elif sospechoso == "AB12":
        print(f"buscando en {sospechoso}\n Sospechoso Encontrado")
        break