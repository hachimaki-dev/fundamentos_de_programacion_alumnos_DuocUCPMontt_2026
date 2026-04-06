#ranking de superheroes

print("Bienvenido al ranking de Super Heroes!")

try:

    misiones_exitosas = int(input("Cuantas misiones exitosas tuvo el heroe este mes?: "))
    daños_civiles = int(input("Y cuantos daños civiles causo?: "))

    if misiones_exitosas >= 10 and daños_civiles == 0:
        print("Heroe categoría S, recibe bono máximo.")

    elif misiones_exitosas >= 5:
        print("Heroe categoría A, cumple promedio.")

    elif misiones_exitosas < 5 and daños_civiles >= 10:
        print("Despedido, demasiado caos.")

    else:
        print("Heroe en observación.")
    
except ValueError:
    print("Ingresa un monto valido.")