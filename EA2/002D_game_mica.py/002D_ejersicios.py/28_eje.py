patente = ['XY11', 'ZZ99', 'AB12', 'XX00']
patente_robada = "AB12"

for vosca_patente in patente:
    print(f"buscando en {vosca_patente}")
    if vosca_patente == patente_robada:
        print("sospechoso encontrado")
        break