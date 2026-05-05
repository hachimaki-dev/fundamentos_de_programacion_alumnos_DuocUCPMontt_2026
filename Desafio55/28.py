patentes = ['XY11', 'ZZ99', 'AB12', 'XX00']
buscar = "AB12"

for patente in patentes:
    print(f"Buscando en {patente} ...")

    if patente == buscar:
        print("Sospechoso encontrado")
        break