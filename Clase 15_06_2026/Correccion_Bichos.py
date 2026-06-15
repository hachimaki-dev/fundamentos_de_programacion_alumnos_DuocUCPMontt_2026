lista_de_todos_los_bichos=[]

def mostrar_menu():
  print("\n========== MENÚ PRINCIPAL ========== ")
  print("1. Ingresar bicho")
  print("2. Buscar bicho")
  print("3. Eliminar bicho")
  print("4. Actualizar estados (nivel de peligrosidad)")
  print("5. Mostar todos los bichos")
  print("6. Salir")
  print("=====================================\n")

def leer_opcion_usuario_menu():
  while True:
    opcion_ingresada = input("Ingrese su opción")
    if 1<=int(opcion_ingresada)<=6:
      return opcion_ingresada
    else:
      print("Opcion invalida, vuelva a intenar")

def validar_nombre_bicho():
  especie_bicho=input("Ingrese la especie del bicho")
  if len(especie_bicho)<=0 or " " in especie_bicho:
    print("El nombre de la especie no es valido")
  else:
    return especie_bicho

def validar_longitud_bicho():
  while True:
    try:
        longitud_bicho=int(input("Ingrese el tamaño del bicho"))
        if longitud_bicho<=0:
            print("La longitud del bicho no es valida")
        else:
            return longitud_bicho
    except ValueError:
        print("Valor invalido, inserte un numero entero")

def validar_peligrosidad_bicho():
  try:
    peligrosidad_bicho=float(input("Ingrese el nivel de peligrosidad del bicho (1.0-10.0)"))
    if 1.0<=peligrosidad_bicho<=10.0:
        return peligrosidad_bicho
    else:
        print("El nivel de peligrosidad del bicho no es valido")
  except ValueError:
    print("El nivel de peligrosidad del bicho no es valido")

def agregar_bicho():
    especie_bicho_validado=validar_nombre_bicho()
    longitud_bicho_validada=validar_longitud_bicho()
    peligrosidad_bicho_validada=validar_peligrosidad_bicho()

    datos_bicho={"Especie": especie_bicho_validado, "Tamaño": longitud_bicho_validada, "Peligrosidad": peligrosidad_bicho_validada, "Es peligroso": peligrosidad_bicho_validada>=7.0}
    lista_de_todos_los_bichos.append(datos_bicho)
    
def mostrar_todos_los_bichos():
    print(lista_de_todos_los_bichos)

def invocar_funcion_buscar_bicho():
    for cada_bicho in lista_de_todos_los_bichos:


def iniciar_programa():
  while True:
    mostrar_menu()
    opcion_menu_usuario_validada = leer_opcion_usuario_menu()
    if opcion_menu_usuario_validada == "1":
      agregar_bicho()
    elif opcion_menu_usuario_validada == "2":
      invocar_funcion_buscar_bicho()
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