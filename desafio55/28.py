patentes = ["XY11", "ZZ99", "AB12", "XX00"]
sospechoso = "AB12"
for patente in patentes:
    print(f"buscando en {patente}...")
    if patente == sospechoso:
        print(f"Sospechoso encontrado")
        break