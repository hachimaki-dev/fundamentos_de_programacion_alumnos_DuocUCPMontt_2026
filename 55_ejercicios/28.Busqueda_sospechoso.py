patentes_vehiculos = ["XY11", "ZZ99", "AB12", "XX00"]
for patente_especifica in patentes_vehiculos:
    print(f"Buscando en {patente_especifica}...")
    if patente_especifica == "AB12":
        print("Sospechoso encontrado")
        break