
senior = 0
junior = 0


while True:
    try:
        cantidad_de_ingenieros_a_registrar = int(input("cuantos ingenieros desea registrar?: "))
        if cantidad_de_ingenieros_a_registrar > 0:
            break
        else:
            print("debes usar un numero mayor a cero")
    except ValueError:
        print("por favor ingrese un valor correcto")



for cada_ingeniero_a_registrar in range(1, cantidad_de_ingenieros_a_registrar + 1):
    while True:
        alias_de_ingeniero = input(f"ingresa alias del ingeniero numero {cada_ingeniero_a_registrar}: ")
        bandera_valida_ingeniero = True
        if len(alias_de_ingeniero) < 6:
            bandera_valida_ingeniero = False
            print("el alias debe tener 6 caracteres")
        
        if " " in alias_de_ingeniero:
            bandera_valida_ingeniero = False
            print("el alias no debe tener espacios en blanco")

        if not alias_de_ingeniero.isalnum():
            bandera_valida_ingeniero = False
            print("el alias del ingeniero no puede contener caracteres especiales, solo numeros y letras")

        if bandera_valida_ingeniero == True:
            print("cumple")
            break
        else:
            print("no cumple con las reglas")


    while True:
        try:
            nivel_del_ingeniero = int(input("cual es el nivel tecnico del ingeniero: "))
            if nivel_del_ingeniero > 0:
                if nivel_del_ingeniero > 45:
                    print("es senior")
                    senior += 1
                    dic_ingeniero = {
                        "nombre": alias_de_ingeniero,
                        "nivel": nivel_del_ingeniero,
                        "categoria": "senior"
                    }
                elif nivel_del_ingeniero <= 45:
                    print("es junior")
                    junior += 1
                    dic_ingeniero = {
                        "nombre": alias_de_ingeniero,
                        "nivel": nivel_del_ingeniero,
                        "categoria": "junior"
                    }
                break   
            else:
                print("debes usar un numero mayor a cero")
        except ValueError:
            print("por favor ingrese un valor correcto")

print(f"la cantidad de ingenieros juniors es")
















