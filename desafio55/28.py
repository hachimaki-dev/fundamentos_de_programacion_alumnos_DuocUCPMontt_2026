patentes = ['XY11', 'ZZ99', 'AB12', 'XX00']
buscada = "AB12"
for i in patentes:
    print("BUSCANDO EN",i)
    if i == buscada:
        print("SOSPECHOSO ENCONTRADO",i)
        break
