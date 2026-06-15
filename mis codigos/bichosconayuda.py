lista_de_todos_los_bichos = []



def mostrar_menu():

  print(f"1. Ingresar bicho")

  print(f"2. Buscar bicho")

  print(f"3. Eliminar bicho")

  print(f"4. Actualizar estado de todos los bichos (si es peligroso o no)")

  print(f"5. Mostrar todos los bichos")

  print(f"6. Salir")



def opcion_menu_usuario():

  while True:

    opcion_elegida = input("Ingrese su opción (1 al 6)")

    if opcion_elegida in ["1", "2", "3", "4", "5", "6"]:

      return opcion_elegida 

    else:

      print("Opción invalida, vuelva a intentarlo")  



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

      longitud_bicho = int(input("Ingrese el tamaño del bicho: \n"))

      if longitud_bicho > 0:

        return longitud_bicho

      else:

        print("La longitud debe ser mayor que cero")

    except ValueError:

      print("Valor no valido")





def validar_peligrosidad_bicho():

  while True:

    try:

      peligrosidad_bicho = float(input("Ingrese el nivel de peligrosidad del bicho: \n"))

      if peligrosidad_bicho >= 1.0 and peligrosidad_bicho <= 10.0:

        return peligrosidad_bicho

      else:

        print("La peligrosidad del bicho debe ser mayor que cero")

    except ValueError:

      print("Valor no valido")


  

def agregar_bicho():

  nombre_bicho_validado = validar_nombre_bicho()

  longitud_bicho_validada = validar_longitud_bicho()

  peligrosidad_bicho_validada = validar_peligrosidad_bicho()



  datos_de_bicho = {

    "nombre_bicho" :nombre_bicho_validado,

    "longitud_bicho" : longitud_bicho_validada,

    "peligrosidad_bicho" : peligrosidad_bicho_validada,

    "es_peligroso" : False

  }



  lista_de_todos_los_bichos.append(datos_de_bicho)





def mostrar_todos_los_bichos():

  print(lista_de_todos_los_bichos)



def iniciar_programa():

  while True:

    mostrar_menu()

    opcion_menu_seleccionada = opcion_menu_usuario()



    if opcion_menu_seleccionada == "1":

      agregar_bicho()

    elif opcion_menu_seleccionada == "2":

      print("Se manda a llamar la funcion que Busca")

    elif opcion_menu_seleccionada == "3":

      print("Se manda a llamar la funcion que elimina")

    elif opcion_menu_seleccionada == "4":

      print("Se manda a llamar la funcion que Actualiza el estado")

    elif opcion_menu_seleccionada == "5":

      mostrar_todos_los_bichos()

    elif opcion_menu_seleccionada == "6":

      print("Adios")

      break

    else:

      print("LA opcion ingresada no es una opción valida")

  



iniciar_programa()