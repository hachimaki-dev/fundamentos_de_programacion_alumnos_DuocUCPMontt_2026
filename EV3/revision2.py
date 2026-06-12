while True:
    try:
        ingeniero_registrar = int(input("Cuantos ingenieros desea registrar?"))
        if ingeniero_registrar > 0:
            break
        else:
            print("Debe ser un numero mayor a 0")
    except ValueError:
        print("Error ingrese un numero")
        
for ingeniero_registrar in range(1, ingeniero_registrar + 1):
    alias_ingeniero = input(f"Ingrese el alias del ingeniero {ingeniero_registrar}")
    validar_alias = True
    
    if len(alias_ingeniero) < 6:
        validar_alias = False
        print("El alias debe contener 6 caracteres o mas")
    
    if " " in alias_ingeniero:
        validar_alias = False
        print("El alias no debe contener espacios en blanco")
        
        

        