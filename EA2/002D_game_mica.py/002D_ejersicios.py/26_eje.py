hojas_diponibles = 5
cola_de_impresion = ["texto" , "foto" , "texto" , "foto"]

for documento in cola_de_impresion
    if documento == "texto" and hojas_diponibles >= 1:
        hojas_diponibles -= 1
        print("imprimindo texto")
        elif documento == "foto" and hojas_diponibles >= 3:
            hojas_diponibles -= 3
            print("imprimiendo foto")
            else:
                print("sin papel")
