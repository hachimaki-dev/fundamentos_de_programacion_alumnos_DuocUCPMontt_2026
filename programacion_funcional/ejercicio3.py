lista_de_animales = []
def menu():
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Registrar animal")
    print("2. Buscar animal")
    print("3. Eliminar animal")
    print("4. Actualizar alertas")
    print("5. Mostrar animales")
    print("6. Salir")
    print("=====================================")

def opcion_usuario_validada():
    opcion_usuario__elejida = input("ingresa una opcion del (1-6): \n")
    if opcion_usuario__elejida in ["1", "2", "3", "4", "5", "6"]:
        return opcion_usuario__elejida
    else:
        print("intenta con una opcion valida")

#"nombre" Nombre del animal No vacío ni solo espacios en blanco
def validar_nombre_animal():
    while True:
        nombre_animal_ingresado_usuario = input("ingresa el nombre del animal :\n").strip()
        if " " in nombre_animal_ingresado_usuario or len(nombre_animal_ingresado_usuario) <=0:
            print("ingresa el nombre del animal sin espacios y no dejes la casilla en blanco")
        else:
            return nombre_animal_ingresado_usuario
    
#"especie"Especie del animal (perro,gato, etc.)No vacío ni solo espacios en blanco
def validar_especie_animal():
    while True:
        nombre_especie_ingresado_usuario = input("ingresa la especie del animal :\n").strip()
        if " " in nombre_especie_ingresado_usuario or len(nombre_especie_ingresado_usuario) <=0:
            print("ingresa el nombre de la especie sin espacios y no dejes la casilla en blanco")
        else:
            return nombre_especie_ingresado_usuario

#"peso"Peso del animal en kilogramos Número decimal mayor que cero
def validar_peso_animal():
    while True:
        try:
            pesoanimal_ingresado_usuario = float(input("ingresa el peso del animal en kilogramos : \n"))
            if pesoanimal_ingresado_usuario <0:
                print("el peso del animal ingresado no puede ser menos que 0, intenta nuevamente")
            else:
                return pesoanimal_ingresado_usuario
        except ValueError:
            print("ingresa un valor en numeros")

def agregar_datos_animal_a_lista():
    nombre_animal_validado = validar_nombre_animal()
    nombre_especie_validada = validar_especie_animal()
    peso_animal_validado = validar_peso_animal()

    datos_animal = {
        "nombre" : nombre_animal_validado,
        "especie": nombre_especie_validada,
        "peso": peso_animal_validado,
        "alerta" : False
    }
    lista_de_animales.append(datos_animal)
    print(lista_de_animales)



def iniciar_programa():
    while True:
        menu()
        opcion_usuario_menu = opcion_usuario_validada()
        if opcion_usuario_menu == "1":
            agregar_datos_animal_a_lista()
        elif opcion_usuario_validada == "2":
            pass
        elif opcion_usuario_validada == "3":
            pass
        elif opcion_usuario_validada == "4":
            pass
        elif opcion_usuario_validada == "5":
            pass
        elif opcion_usuario_menu == "6":
            break

iniciar_programa()