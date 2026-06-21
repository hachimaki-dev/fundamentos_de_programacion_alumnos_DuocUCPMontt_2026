lista_de_todos_los_bichos = []



def mostrar_menu():

  print(f"1. Ingresar bicho")

  print(f"2. Buscar bicho")

  print(f"3. Eliminar bicho")

  print(f"4. Actualizar estados (nivel de peligrosidad)")

  print(f"5. Mostar todos los bichos")

  print(f"6. Salir")



def leer_opcion_usuario_menu():

  while True:

    opcion_ingresada = input("Ingrese su opción")

    if opcion_ingresada in ["1", "2", "3", "4", "5", "6"]:

      return opcion_ingresada

    else:

      print("Opcion invalida, vuelva a intenar")





def validar_nombre_bicho():

  especie_bicho = input("Ingrese la especie del bicho")

  if len(especie_bicho) <= 0 or " " in especie_bicho:

    print("El nombre de la especie no es valido")

  else:

    return especie_bicho



def validar_longitud_bicho():

  while True:

    try:

      longitud_bicho = int(input("Ingrese el tamaño del bicho"))

      if longitud_bicho <= 0:

        print("Ingrese una longitud superior a 0")

      else:

        return longitud_bicho

    except ValueError:

      print("Valor invalido, inserte un número entero")





def validar_peligrosidad_bicho():

  while True:

    try:

      peligrosidad_bicho = int(input("Ingrese la peligrosidad del bicho"))

      if peligrosidad_bicho >= 1.0 and peligrosidad_bicho <= 10.0:

        return peligrosidad_bicho

      else:

        print("Por favor ingrese un rango valido (entre 1.0 y 10.0)")

    except ValueError:

      print("Valor invalido, inserte un número entero")



  

def agregar_bicho():

  especie_bicho_validado = validar_nombre_bicho()

  longitud_bicho_validada = validar_longitud_bicho()

  peligrosidad_bicho_validada = validar_peligrosidad_bicho()

  

  print(f"El nombre del bicho es {especie_bicho_validado} su tamaño es {longitud_bicho_validada} y su nivel de peligrosidad es: {peligrosidad_bicho_validada}")



  datos_del_bicho = {

    "especie_bicho" : especie_bicho_validado,

    "longitud_bicho" : longitud_bicho_validada,

    "peligrosidad_bicho" : peligrosidad_bicho_validada,

    "es_peligroso" : True

  }



  lista_de_todos_los_bichos.append(datos_del_bicho)





def mostrar_todos_los_bichos():

  print(lista_de_todos_los_bichos)



def inciar_programa():

  while True:

    mostrar_menu()

    opcion_menu_usuario_validada = leer_opcion_usuario_menu()



    if opcion_menu_usuario_validada == "1":

      agregar_bicho()

    elif opcion_menu_usuario_validada == "2":

      print("Invocar funcion que busca bicho")

    elif opcion_menu_usuario_validada == "3":

      print("Invocar funcion que busca Elimina")

    elif opcion_menu_usuario_validada == "4":

      print("Invocar funcion que actualiza los estados del bicho")

    elif opcion_menu_usuario_validada == "5":

      mostrar_todos_los_bichos()

    elif opcion_menu_usuario_validada == "6":

      print("Salimos")

      break

    else:

      print("Opcion no pemritida")







inciar_programa()