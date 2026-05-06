patentes = [ "XY11", "ZZ99", "AB12", "XX00" ]
patente_sospechosa = "AB12"

for i in patentes:
    print(f"Buscando en {i}...")
    if i == patente_sospechosa:
        print("SOSPECHOSO ENCONTRADO")
        break
    else:
        pass
