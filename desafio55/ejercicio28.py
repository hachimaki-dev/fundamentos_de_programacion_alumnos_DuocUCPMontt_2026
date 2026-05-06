patentes = ['XY11', 'ZZ99', 'AB12', 'XX00']

for patente in patentes:
    print(patente)
    if patente != "AB12":
        print(f"Buscando en {patente}, auto no robado pasando al siguiente.")
    else:
        print(f" {patente} AUTO ROBADO ENCONTRADO")
        break