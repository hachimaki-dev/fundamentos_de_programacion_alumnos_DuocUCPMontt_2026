patentes = ['XY11', 'ZZ99', 'AB12', 'XX00']
for patente in patentes:
    if patente == "AB12":
        print(f"buscando en {patente}")
        print("Sospechoso encontrado")
        break
    else:
        print(f"buscando en {patente}")