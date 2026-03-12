capuccinoRico = "Capuccino rico"
cafe = "Café"
te = "Té"
milo = "Milo"

opciones = []

opciones.append(capuccinoRico)
opciones.append(cafe)
opciones.append(te)
opciones.append(milo)

def MostrarInicio():
    print("- Bienvenido a Café Bonito -")
    MostrarMenu()
    numOpcion = int(input("Por favor, seleccione su opción:"))
    print("¿Quiere comprar " + opciones[numOpcion - 1] + "?")
    print("=== FIN DEL PROGRAMA ===")

def MostrarMenu():
    for i in range(len(opciones)):
        print(f"{i+1}) " + opciones[i])

MostrarInicio()