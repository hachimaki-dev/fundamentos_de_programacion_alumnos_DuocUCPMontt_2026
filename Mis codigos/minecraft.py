while True :
    Eleccion = int(input("Selecione una Receta: 1.Craftear Espada de diamante  2.Craftear Pico  3.Salir de la mesa de Crafteo: "))
    if Eleccion == 1 :
        print("Espada crafteada")
    elif Eleccion == 2 :
        print("Pico listo")
    elif Eleccion  == 3 :
        print("Mesa de Crafteo cerrada")
        break
    elif Eleccion != 1 or 2 or 3 :
        print("Receta Desconocida")