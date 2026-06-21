def registrar_ingenieros():

    contador_de_ingenieros_junior = 0
    contador_de_ingenieros_senior = 0
    lista_de_ingenieros = []

    
    while True:
        try:
            cantidad_de_ingenieros_a_registrar = int(input("¿Cuántos ingenieros desea registrar? "))
            if cantidad_de_ingenieros_a_registrar > 0:
                break
            else:
                print("Debe ser un número superior a cero")
        except ValueError:
            print("Error, valor no válido")

    for cada_ingeniero_a_registrar in range(1, cantidad_de_ingenieros_a_registrar + 1):
        while True:
            alias_del_ingeniero = input(f"Por favor ingrese el alias del ingeniero n° {cada_ingeniero_a_registrar} : \n")
            bandera_validando_alias = True
            
            if len(alias_del_ingeniero) < 6:
                print("El alias debe contener al menos 6 caracteres")
                bandera_validando_alias = False

            if " " in alias_del_ingeniero:
                bandera_validando_alias = False
                print("El alias no debe contener espacios")

            if not alias_del_ingeniero.isalnum():
                bandera_validando_alias = False
                print("El alias no debe contener caracteres especiales")

            if bandera_validando_alias == True:
                break
            else:
                print("Sucedió un error con el alias, intente de nuevo.")

        while True:
            try:
                nivel_tecnico_del_ingeniero = int(input("¿Cuál es el nivel técnico del ingeniero/a ?: \n"))
                if nivel_tecnico_del_ingeniero > 0:
                    if nivel_tecnico_del_ingeniero > 45:
                        print("Senior")
                        contador_de_ingenieros_senior += 1
                        diccionario_de_ingeniero = {"alias": alias_del_ingeniero, "nivel": nivel_tecnico_del_ingeniero, "categoria": "senior"}
                    else:
                        print("Junior")
                        contador_de_ingenieros_junior += 1
                        diccionario_de_ingeniero = {"alias": alias_del_ingeniero, "nivel": nivel_tecnico_del_ingeniero, "categoria": "junior"}

                    lista_de_ingenieros.append(diccionario_de_ingeniero)
                    break
                else:
                    print("Debe ser un número superior a cero")
            except ValueError:
                print("Error, valor no válido")

    
    print("\n--- RESUMEN DE REGISTRO ---")
    print(f"La cantidad de ingenieros juniors es {contador_de_ingenieros_junior} y de seniors es {contador_de_ingenieros_senior}")
    print(f"La lista de todos los ingenieros es: \n{lista_de_ingenieros}")
    
    
    return {
        "ingenieros": lista_de_ingenieros,
        "total_juniors": contador_de_ingenieros_junior,
        "total_seniors": contador_de_ingenieros_senior
    }