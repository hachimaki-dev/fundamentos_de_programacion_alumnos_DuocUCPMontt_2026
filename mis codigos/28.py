patentes = ['XY11', 'ZZ99','XX00', 'AB12']

for patente in patentes:

    if patente != "AB12":
        print (f"Revisando patente... {patente}")

    elif patente == "AB12":
        print(f"¡SOSPECHOSO ENCONTRADO PATENTE  {patente}.")
        break