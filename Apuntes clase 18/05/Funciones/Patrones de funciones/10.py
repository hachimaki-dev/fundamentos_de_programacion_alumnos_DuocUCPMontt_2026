def pedir_edad_valida():
    while True:
        entrada = input("Edad: ")
        if entrada.isdigit() and int(entrada) > 0:
            return int(entrada)
        else:
            print("Edad inválida")