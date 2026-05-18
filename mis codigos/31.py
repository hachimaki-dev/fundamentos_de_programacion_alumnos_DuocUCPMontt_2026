Lista_canciones = ["B", "C"]

insertar_D = input("Ingresar cancion D? (SI/NO): ").lower

if insertar_D == "si":
    Lista_canciones.append("D")

insertar_A = input("Ingresar cancion A? (SI/NO): ").lower

if insertar_A == "si":
    Lista_canciones.insert(0, "A")

print("Lista_canciones", Lista_canciones)