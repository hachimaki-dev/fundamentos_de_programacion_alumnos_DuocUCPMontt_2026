patentes_guardadas = ["XY11", "ZZ99", "AB12", "XXOO"]

for patente in patentes_guardadas:
    print(f"Buscando {patente}")
    if patente == "AB12":
        print("Sospechoso encontrado")
        break