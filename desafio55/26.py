hojas_restantes= 5
cola_impresion= ['texto', 'foto', 'texto', 'foto']

for documento in cola_impresion:
    if documento == "texto" and hojas_restantes >= 1:
        hojas_restantes -= 1
        print(f"Imprimiendo {[documento]}")
    elif documento == "foto" and hojas_restantes >= 3:
        hojas_restantes -= 3
        print(f"Imprimiendo {[documento]}")
    else:
        print("No hay papel")