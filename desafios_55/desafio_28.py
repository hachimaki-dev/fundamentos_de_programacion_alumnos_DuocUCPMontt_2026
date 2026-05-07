patentes = ['XY11', 'ZZ99', 'AB12', 'XX00']

for patente in patentes:
    print(f"Buscando en {patente}...")
    if patente == "AB12":
        print("Sospechoso encontrado")
        break