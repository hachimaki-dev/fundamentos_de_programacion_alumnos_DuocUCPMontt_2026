patentes = ["XY11","ZZ99","AB12","XX00"]

buscando = "AB12"

for i in patentes :
    print(f"Buscando {i}")
    if i == buscando :
        print("Sospechoso encontrado")
        break