senior = 0
junior = 0



ingenieros = []

while True:
    try:
        registro = int(input("cuantos ingenieros quiere registrar?: "))
        if registro > 0:
            break
        else:
            print("dato invalido, ingresa un entero positivo para continuar el registro")
    except ValueError:
            print("dato invalido, ingresa un entero positivo para continuar el registro")

    
for i in range(registro):
    while True:
        try:
            alias = input(f"cual es el alias del ingeniero numero {i+1}: ")
            if len(alias) >= 6 and " " not in alias:
                break
            else:
                print("error, tiene que tener al menos 6 caracteres y sin espacios")
        except ValueError:
                print("error, tiene que tener al menos 6 caracteres y sin espacios")
                
    while True:
        try:
            nivel = int(input(f"en que nivel esta el ingeniero nuemro {i+1}?: "))
            if nivel > 0:
                break
            else:
                print("error, tiene que ser un numero positivo")
        except ValueError:
            print("error, tiene que ser un numero positivo")
        
        
        
    if nivel > 45:
        categoria = "senior"
        print("esta en nivel senior")
        senior += 1
    else:
        categoria = "junior"
        print("esta en nivel junior")
        junior += 1
            
    ingeniero = {
        "alias": alias,
        "nivel": nivel,
        "categoria": categoria
        }
        
    ingenieros.append(ingeniero)
        



print(f"\nEl instituto cuenta con {senior} Ingenieros Senior y {junior} Ingenieros Junior ¡Registro completado satisfactoriamente!")
