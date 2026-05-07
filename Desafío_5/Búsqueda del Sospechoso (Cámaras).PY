Patentes = ["XY11", "ZZ99", "AB12", "XX00"]

for i in Patentes:
    print (f"Buscando en ", i )

    if i == "AB12":
        print(f"Encontramos al sospechoso, es la PATENTE {i}")
        break