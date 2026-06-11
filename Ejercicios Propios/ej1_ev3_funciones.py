datos_de_los_ingenieros = []
contador_ingenieros_junior = 0
contador_ingenieros_senior = 0

def registro_de_los_ingenieros():
    while True:
        try:
            ingenieros_a_registrar = int(input("Ingrese cuantos ingenieros se van a Registrar : "))
            if ingenieros_a_registrar <= 0:
                print("Ingrese un numeo entero positivo ")
            else:
                break
        except ValueError:
            print("Ingrese una opcion valida") 

    def proceso_del_registro():
        for i in range(ingenieros_a_registrar):
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

            datos_de_los_ingenieros.append({"nombre" : alias_ingeniero ,"Nivel Tecnico" : nivel_tecnico , "Titulo" : titulo })

    proceso_del_registro()

    def Historial_de_los_ing_registrados():
        print("\n==== Registro de Ingeniero ===== \n")
        for ing in datos_de_los_ingenieros:
            print(f"Nombre : {ing["nombre"]} | Nivel Tecnico : {ing["Nivel Tecnico"]} | Titulo : {ing["Titulo"]}")

    Historial_de_los_ing_registrados()

registro_de_los_ingenieros()