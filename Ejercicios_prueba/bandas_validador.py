print(">>>>>>BIENVENIDO<<<<<<")

eleccion_usuario= ""

while eleccion_usuario != "los bunkers" or "los prisioneros" or "los tres":
    eleccion_usuario= input("Ingresa tu banda favorita (Rock Chileno): ").lower()
    if eleccion_usuario == "los bunkers":
        print("FELICIDADES! ENTRASTE AL FANDOM")
        break
    elif eleccion_usuario == "los prisioneros":
        print("FELICIDADES! ENTRASTE AL FANDOM")
        break
    elif eleccion_usuario == "los tres":
        print("FELICIDADES! ENTRASTE AL FANDOM")
        break
    else:
        print("INGRESA UNA OPCION VALIDA")
        continue

print("GRACIAS POR PARTICIPAR")