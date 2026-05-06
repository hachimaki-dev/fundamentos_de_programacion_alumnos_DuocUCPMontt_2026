patentes = ["XY11", "ZZ99", "AB12", "XX00"]
buscamos = "AB12"
for i in patentes:
    print(F"buscando en {i}")
    if i == "AB12":
        print("sospechoso encontrado")
        break