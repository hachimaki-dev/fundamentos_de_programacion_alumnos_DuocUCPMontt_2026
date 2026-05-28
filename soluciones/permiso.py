edad_del_usuario = 0

while True:
    try:
        edad_del_usuario = int(input("ingrese su edad: "))
        if edad_del_usuario > 0:
            print(f"Edad registrada: {edad_del_usuario} años")
            break
        elif edad_del_usuario <=0:
            print("tiene que ser un numero positivo")
    except:
        print("nada de letras o fracciones")