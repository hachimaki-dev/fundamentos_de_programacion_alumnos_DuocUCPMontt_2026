contador_ingenieros_junior = 0
contador_ingenieros_senior = 0


while True:
    try:
        Cantidad_de_ingenieros_a_registrar = int(input("¿Cuantos ingenieros desea registrar?"))
        if Cantidad_de_ingenieros_a_registrar > 0:
            break
        else:
            print("Debe ser un numero superior a cero")
    except ValueError:
        print("Porfavor ingrese un valor correcto")

for cada_ingeniero_a_registrar in range(1,Cantidad_de_ingenieros_a_registrar + 1):
    while True:
        alias_del_ingeniero = input(f"Ingrese el alias del inge N° {cada_ingeniero_a_registrar}")
    
        bandera_validando_alias_del_ingeniero = True
        if len(alias_del_ingeniero) < 6:
            bandera_validando_alias_del_ingeniero = False
            print("Warning!, el alias debe contener 6 caracteres o mas de longitud")
        if " " in alias_del_ingeniero:
            bandera_validando_alias_del_ingeniero = False
            print("Warning!!, El alias no debe contener espacios en blanco")
        if not alias_del_ingeniero.isalnum():
            bandera_validando_alias_del_ingeniero = False
            print("Warning!!, El alias del ingeniero no puede contener caracteres especiales. Solo ingrese numero o letras")
        if bandera_validando_alias_del_ingeniero == True:
            print("ea")
        else:
            print("No cumplio con una o mas de una regla de validacion")
    while True:
        try:
            Nivel_tecnico_del_ingeniero = int(input("¿Cual es el nivel tecnico del ingeniero?"))
            if  Nivel_tecnico_del_ingeniero> 0:
                if Nivel_tecnico_del_ingeniero > 45:
                    print("Es Senior")
                    diccionario_de_ingenieros = {"Alias": alias_del_ingeniero,"nivel": Nivel_tecnico_del_ingeniero, "categoria": "Junior"}
    
                elif Nivel_tecnico_del_ingeniero <= 45:
                    print("Junior")
            else:
                print("Debe ser un numero superior a cero")
        except ValueError:
            print("Porfavor ingrese un valor correcto")