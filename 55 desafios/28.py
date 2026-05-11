patentes = ["XY11", "ZZ99", "AB12", "XX00"]

for patente in patentes:

    if patente != "AB12":
        print(f"Buscando en {patente}")
    elif patente == "AB12":
        print(f"Buscando en {patente}... \nSospechoso encontrado")
        break

