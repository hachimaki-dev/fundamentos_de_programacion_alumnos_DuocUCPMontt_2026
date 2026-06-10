senior = 0
junior = 0
list_senior = []
list_junior = []

while True:
    try:
        cantidad_de_ingenieros_a_registrar = int(input("¿Cuántos ingenieros desea registrar?"))
        if cantidad_de_ingenieros_a_registrar > 0:
            break
        else:
            print("Debej ser un número superior a 0.")
    except ValueError:
        print("Por favor ingrese un valor correcto.")

for cada_ingeniero_a_registrar in range(1, cantidad_de_ingenieros_a_registrar + 1):
    while True:
        alias_del_ingeniero = input(f"Ingrese el alias del ingeniero N°{cada_ingeniero_a_registrar}: ")
        bandera_validando_alias_del_ingeniero = True
        #Si tiene menos de 6 caracteres, no cumple :(
        if len(alias_del_ingeniero) < 6:
            bandera_validando_alias_del_ingeniero = False
            print("WARNING!!!: EL alias debe contener 6 caracteres o más de longitud.")
        #si tiene espacios, no cumple
        if " " in alias_del_ingeniero:
            bandera_validando_alias_del_ingeniero = False
            print("WARNING!!: El alias no debe contener espacios en blanco.")
        #Si tiene caracteres especiales, no cumple
        if not alias_del_ingeniero.isalnum() == False:
            print("WARNING!!: El alias no puede conter caracteres espaciales, solo números y letras.")
        #Si tiene todo correcto :D
        if bandera_validando_alias_del_ingeniero:
            break
        else:
            print("No se cumplieron una o más reglas de calidación del alias")
    
    while True:
        try:
           nivel_tecnico_del_ingeniero = int(input(f"¿Cuál es el nivel técnico del ingeniero {alias_del_ingeniero}?"))
           if nivel_tecnico_del_ingeniero > 0:
                if nivel_tecnico_del_ingeniero > 45:
                    senior += 1
                    diccionario_senior = {"alias":alias_del_ingeniero, "nivel":nivel_tecnico_del_ingeniero, "categoria":"senior"}
                    list_senior.append(diccionario_senior)
                    print("Es senior.")
                elif nivel_tecnico_del_ingeniero <= 45:
                    junior += 1
                    diccionario_junior = {"alias":alias_del_ingeniero, "nivel":nivel_tecnico_del_ingeniero, "categoria":"junior"}
                    list_junior.append(diccionario_junior)
                    print("Es junior.")
                break
           else:
                print("Debej ser un número superior a 0.")
        except ValueError:
            print("Por favor ingrese un valor correcto.")

 