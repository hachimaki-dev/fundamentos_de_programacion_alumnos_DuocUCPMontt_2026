datos_ingeniero = []

while True:
    try:
        registrar_ingenieros = int(input("Ingrese cuantos ingenieros se van a Registrar : "))
        if registrar_ingenieros <= 0:
            print("Ingrese un numeo entero positivo ")
        else:
            break
    except ValueError:
        print("Ingrese una opcion valida")        

for i in range(registrar_ingenieros):

    while True:
        alias_ingeniero = input("Ingrese su Nombre Clave: ").lower()
        if len(alias_ingeniero) < 6 or " " in alias_ingeniero:
            print("Ingrese un nombre de Minim 6 caracteres y sin espacios")
        else:
            break
        
    while True:
        try:
            nivel_tecnico= int(input("Ingrese Cual es su nivel tecnico: "))
            if nivel_tecnico <= 0:
                print("Ingrese un numero entero positivo ")
            elif nivel_tecnico > 45:
                titulo = "Ingeniero Senior"
                break
            else:
                titulo = "Ingeniero Junior"
                break
        except ValueError:
            print("Ingrese una opcion valida")
        
    datos_ingeniero.append({"nombre" : alias_ingeniero ,"Nivel Tecnico" : nivel_tecnico , "Titulo" : titulo })

print()
print("==== Registro de Ingeniero ===== ")
for ing in datos_ingeniero:

    print(f"Nombre : {ing["nombre"]} | Nivel Tecnico : {ing["Nivel Tecnico"]} | Titulo : {ing["Titulo"]}")