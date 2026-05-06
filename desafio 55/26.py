hojas_disponibles = 5
cola_impresion = ['TEXTO', 'FOTO', 'TEXTO', 'FOTO']

for documento in cola_impresion:
    # Definimos el costo de cada tipo de documento
    costo = 1 if documento == 'TEXTO' else 3
    
    # Revisamos si hay papel suficiente
    if hojas_disponibles >= costo:
        hojas_disponibles -= costo
        print(f"Imprimiendo {documento}")
    else:
        print("Sin papel")
        break
