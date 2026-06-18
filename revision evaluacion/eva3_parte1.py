contador_de_ingenieros_junior = 0
contador_de_ingenieros_senior = 0
lista_de_ingenieros = []

while True:
    try:
        cantidad_de_ingenieros_a_registrar = int(input("¿Cuantos ingenieros desea registrar?: "))
        if cantidad_de_ingenieros_a_registrar > 0:
            break
        else:
            print("Ingrese un numero mayor que cero")
    except ValueError:
        print("Ingrese un valor correcto")

for cada_infeniero_a_ingresar in range(1, cantidad_de_ingenieros_a_registrar):
    while True:
        alias_del_ingeniero = input("Infrese alias del ingenieroi: ")
        bandera_balidando_alias = True

        if len(alias_del_ingeniero) < 6:
            bandera_balidando_alias = False
            print("El alias debe contener 6 o más caraceteres")

        if " "in alias_del_ingeniero:
            bandera_balidando_alias = False
            print("El alias no debe contener espacios")

        if not alias_del_ingeniero.isalnum():
            bandera_balidando_alias = False
            print("El alias debe contener solo letras y/o numeros, nada de caracteres especiales.")

        if bandera_balidando_alias == True:
            break
        else:
            print("Algo salio mal")

    while True:
        try:
            nivel_del_ingeniero_registrado = int(input("¿Cuantos ingenieros desea registrar?: "))
            if nivel_del_ingeniero_registrado > 0:
                if nivel_del_ingeniero_registrado > 45:
                    print("Senior")
                    contador_de_ingenieros_senior += 1
                    diccionario_de_ingeniero_senior = {
                        "alias" : alias_del_ingeniero,
                        "nivel" : nivel_del_ingeniero_registrado,
                        "categoria" : "Senior"
                        }
                else:
                    print("Junior")
                    contador_de_ingenieros_junior += 1
                    diccionario_de_ingeniero_junior = {
                        "alias" : alias_del_ingeniero,
                        "nivel" : nivel_del_ingeniero_registrado,
                        "categoria" : "Junior"
                        }

                break
            else:
                print("Ingrese un numero mayor que cero")
        except ValueError:
            print("Ingrese un valor correcto")