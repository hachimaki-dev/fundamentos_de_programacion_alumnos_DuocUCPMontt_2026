lista_bichos = []

def mostrar_menu():
    print("======= MENÚ =======")
    print("1: Ingresar bicho")
    print("2. Buscar bichos")
    print("3. Eliminar bicho")
    print("4. Actualizar estado (si es peligroso o no)")
    print("5. Mostrar bichos")
    print("6. Salir")

def opcion_menu_usuario():
    while True:
        opcion_elegida = input("Ingrese una de estas opciones (1-6): ")
        if opcion_elegida in ["1", "2", "3", "4", "5", "6"]:
            return opcion_elegida
        else:
            print("Opción inválida, vuelve a intentarlo")

def validar_nombre_bicho():
  while True:
    nombre_bicho = input("Ingrese nombre del bicho: \n")
    if " " in nombre_bicho or len(nombre_bicho) <= 0:
        print("Nombre invalido, vuelva a intentar")
    else:
        return nombre_bicho

def validar_longitud_bicho():
    while True:
        try:
            longitud_bicho = int(input("Ingrese la longitud del bicho en cm: "))
            if longitud_bicho > 0:
                return longitud_bicho
            else:
                print("La longitud debe ser mayor que cero")
        except ValueError:
            print("Debe ser un número entero")

def validar_peligrosidad_bicho():
    while True:
        try:
            peligrosidad_bicho = float(input("Ingrese la peligrosidad del bicho (1.0 - 10.0): "))
            if peligrosidad_bicho >= 1.0 and peligrosidad_bicho <= 10.0:
                return peligrosidad_bicho
            else:
                print("Debe estar entre 1.0 y 10.0")
        except ValueError:
            print("Debe ser un número decimal")

def agregar_bicho():
    nombre_bicho_validado = validar_nombre_bicho()
    longitud_bicho_validado = validar_longitud_bicho()
    peligrosidad_bicho_validado = validar_peligrosidad_bicho()
    datos_bicho = {"Nombre especie": nombre_bicho_validado, "Longitud especie": longitud_bicho_validado, "Peligrosidad especie": peligrosidad_bicho_validado, "Es peligroso": False}
    lista_bichos.append(datos_bicho)
    print("¡Bicho registrado exitosamente!")

def buscar_bicho():
    nombre_bicho_buscar = input("Ingrese el nombre del bicho: ")
    for cada_bicho in lista_bichos:
        if cada_bicho["Nombre especie"] == nombre_bicho_buscar:
            print("¡Bicho encontrado!")
            print(f"Su nombre: {cada_bicho["Nombre especie"]}")
            print(f"Su longitud: {cada_bicho["Longitud especie"]}")
            print(f"Su peligrosidad: {cada_bicho["Peligrosidad especie"]}")
        else:
            print("¡Bicho no encontrado!")

def mostrar_bichos():
    print(lista_bichos)

def iniciar_programa():
    mostrar_menu()
    while True:
        opcion_menu_seleccionada = opcion_menu_usuario()
        if opcion_menu_seleccionada == "1":
            agregar_bicho()
        elif opcion_menu_seleccionada == "2":
            buscar_bicho()
        elif opcion_menu_seleccionada == "3":
            print("ELIMINAR BICHO")
        elif opcion_menu_seleccionada == "4":
            print("ACTUALIZAR ESTADO")
        elif opcion_menu_seleccionada == "5":
            mostrar_bichos()
        elif opcion_menu_seleccionada == "6":
            print("Gracias por usar el Cazabichos. ¡Hasta la próxima expedición!")
            break
        else:
            print("La opciòn ingresada no es válida")

iniciar_programa()