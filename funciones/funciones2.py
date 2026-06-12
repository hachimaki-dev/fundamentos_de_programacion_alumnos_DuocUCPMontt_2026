habitaciones_disponibles = 50


def mostrarMenu():

  print("=== MENÚ PRINCIPAL ===")
  print("1. Habitaciones disponibles")  
  print("2. Realizar Check-In")  
  print("3. Realizar Check-Out")  
  print("4. Historial de ocupaciones")  
  print("5. Salir")


def preguntarOpcion():

  while True:
    try:
      opcion_validada_por_funcion = int(input("Ingrese su opción: "))
      break
    except ValueError:
      print("Ingrese opcion valida")
  return opcion_validada_por_funcion

def mostrarHabitacionesDisponibles():
  return habitaciones_disponibles


def ejecutarOpcionMenu():
  opcion = preguntarOpcion()
  if opcion == 1:
    #VOy a llamar a la funcion Habitaciones disponibles
    respuestaHabitacionesDisponibles = mostrarHabitacionesDisponibles()
    print(f"Actualmente hay {respuestaHabitacionesDisponibles} habitaciones disponibles.")
  elif opcion == 2:
    #VOy a llamar a la funcion checkIn
    print("b")
  elif opcion == 3:
    #VOy a llamar a la funcion checkout
    print("b")


  elif opcion == 4:
    #VOy a llamar a la funcion de habitaciones ocupadas
    print("b")
  elif opcion == 5:
    print("b")
  else:
    print("Ingrese opcion valida")

    





#Primero mostramos el menu

mostrarMenu()

ejecutarOpcionMenu()