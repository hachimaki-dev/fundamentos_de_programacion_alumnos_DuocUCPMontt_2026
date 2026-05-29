
while True:
    try:
        edad_del_conductor = int(input("Ingrese su edad :  "))
        if edad_del_conductor <= 0:
            print("Error : coloque un numero entero/positivo")
            continue
        else:
            print(f"Edad Registrada : {edad_del_conductor} años")
            break
    except ValueError:
        print("Error : coloque un numero entero/positivo")