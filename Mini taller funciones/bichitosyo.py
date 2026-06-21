coleccion_de_bichitos = []
def Mostrar_menu ():
    print("==== MENÚ PRINCIPAL ====")
    print("1. Agregar bicho\n2. Buscar bicho\n3. Eliminar bicho\n4. Actualizar estados\n5. Mostrar bichos\n6. Salir")
def opcion_menu_elegida():
  while True:
    opcion_elegida = input("Ingrese una opción\n")
    if opcion_elegida in ["1", "2", "3", "4", "5", "6"]:
      return opcion_elegida
    else:
      print("Opcion invalida, intente nuevamente")

#VALIDACIONES
def validacion_nombre():
    while True:
        nombre_bicho = input("Ingrese el nombre del bicho: ")
        if len(nombre_bicho) <= 0:
            print("Nombre invalido, intente denuevo")
        else:
           return nombre_bicho
def validacion_longitud_bicho():
    while True:
        try:
            longitud_bicho = int(input("Ingrese el tamaño del bicho en cm: "))
            if longitud_bicho <= 0:
                print("ERROR, ingresa numeros mayores a cero.")
            else:
               return longitud_bicho
        except ValueError:
           print("ERROR, no puede ingresar numeros negativos ni decimales.")
def validacion_peligrosidad_bicho():
    while True:
        try:
            peligrosidad_bicho = float(input("Ingrese el nivel de peligrosidad del bicho en una escala de 1.0 a 10.0: "))
            if (peligrosidad_bicho >= 1.0) and (peligrosidad_bicho <= 10.0):
               return peligrosidad_bicho
            else:
               print("Error, ingrese un numero dentro del rango.")
        except ValueError:
           print("ERROR, ingrese numeros decimales correctos y dentro del rango.")
#OPCIÓN N°1
def agregar_bichito():
    nombre_bicho = validacion_nombre()
    longitud_bicho = validacion_longitud_bicho()
    peligrosidad_bicho = validacion_peligrosidad_bicho()
    nuevo_bicho = {"nombre":nombre_bicho.lower(), "longitud":longitud_bicho, "peligrosidad":peligrosidad_bicho, "peligro": False}
    coleccion_de_bichitos.append(nuevo_bicho)
#OPCIÓN N°2
def Buscar_bichito(Name_bug_parameter):
    for i in coleccion_de_bichitos:
        if i["nombre"] == Name_bug_parameter:
            indice_bichito = coleccion_de_bichitos.index(i)
            return indice_bichito
        else:
           print("No se ha podido encontrar este bichito.")
           return False
#OPCIÓN N°3
def Eliminar_bichito(Name_bug_parameter):
   respuestaindice = Buscar_bichito(Name_bug_parameter)
   if coleccion_de_bichitos.pop(respuestaindice):
      return True
   else:
      False
#OPCIÓN N°4
def Actualización_estado(lista):
    for i in lista:
        if i["peligrosidad"] >= 7.0:
           i["peligro"] = True
#OPCIÓN N°5
def Mostrar_bichos(lista):
   for i in lista:
      print(f"Nombre: {i["nombre"]} | Longitud: {i["longitud"]} | Peligrosidad: {i["peligrosidad"]} | Peligro: {i["peligro"]}")
      
def inicio_programa():
    while True:
        Mostrar_menu()
        opcion_elegida_validada = opcion_menu_elegida()
        if opcion_elegida_validada == "1":
           agregar_bichito()
        elif opcion_elegida_validada == "2":
           nombre_del_bicho_buscado = validacion_nombre()
           respuesta_buscando_bicho = Buscar_bichito(nombre_del_bicho_buscado.lower())
           print(f"La respuesta de buscando bicho es: {respuesta_buscando_bicho}.")
        elif opcion_elegida_validada == "3":
            nombre_del_bicho_buscado = validacion_nombre()
            r_eliminando_bug = Eliminar_bichito(nombre_del_bicho_buscado)
            if r_eliminando_bug == True:
               print("Eliminado")
            else:
               print("No se puede eliminar algo que no existe.") 
        elif opcion_elegida_validada == "4":
           Actualización_estado(coleccion_de_bichitos)
        elif opcion_elegida_validada == "5":
           Mostrar_bichos(coleccion_de_bichitos)
        elif opcion_elegida_validada == "6":
           print("Gracias por usar el Cazabichos. ¡Hasta la próxima expedición!")
           break
        else:
           print("ERROR, escoja una opcion valida.")
#UNICA LINEA QUE SE EJECUTA.
inicio_programa()