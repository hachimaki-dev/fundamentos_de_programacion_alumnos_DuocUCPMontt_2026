patentes = ['XY11', 'ZZ99', 'AB12', 'XX00']
patente_buscada = "AB12"
contador = 0

for i in patentes:
    print(f"Buscando patente...{i}")
    if i == patente_buscada:
        print("SOSPECHOSO ENCONTRADO")
        break
    


