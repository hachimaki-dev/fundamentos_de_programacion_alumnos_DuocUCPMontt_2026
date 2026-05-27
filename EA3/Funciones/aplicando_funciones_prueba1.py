def solicitar_datos():
    edad = int(input("Ingrese su edad: "))
    tramo = input("Ingrese su tramo: ")
    return edad, tramo

    

while True:
    edad, tramo = solicitar_datos()

    if edad > 30:
        print("test")
