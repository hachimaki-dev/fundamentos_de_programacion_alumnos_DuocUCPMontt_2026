def pedir_edad_valida_v2():
    while True:
        entrada = input("Edad: ")
        try:
            edad = int(entrada)
            if edad > 0:
                return edad
            else:
                print("Mayor que 0")
        except ValueError:
            print("No es número")