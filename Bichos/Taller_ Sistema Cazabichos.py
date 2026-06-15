#Definir variables (lista vacía para el diccionario de cada bicho)
lista_bichos = []
menu = ["1", "2", "3", "4", "5", "6"]

#Definir las funciones principales para la creación de nuestro programa

#Mostrar el menú
def mostrarMenu():
    print("""========== MENÚ PRINCIPAL ==========
1. Agregar bicho
2. Buscar bicho
3. Eliminar bicho
4. Actualizar estados
5. Mostrar bichos
6. Salir
=====================================""")
    
#Pedir la opción al usuario 
def leerOpcion():
    while True:
        opcion = input("Seleccione una opción: ")
        if opcion in menu:
            return opcion
        else:
            print("Ingrese una opción válida, intentelo de nuevo.")

#Ahora vamos a agregar el bicho
#Nombre de la especie
def validarNombreDelaEspecie():
    while True:
        nombre_especie =input("Ingrese la espcie del bicho: \n").lower().strip()
        if " " in nombre_especie or len(nombre_especie) < 0:
            print("Ingrese un nombre válido")
        else:
            return nombre_especie

#Ahora validaremos el tamaño del bicho, debe ser mayor a 0
def validarTamanioDeLaEspecie():
     while True:
        longitud_especie = int(input("Ingrese tamaño de la especie: \n"))
        if longitud_especie <= 0:
             print("El tamaño del bicho debe ser mayor a 0.")
        else:
             return longitud_especie

#Es momento de validar la peligrosidad del bicho debe ser mayor a 0 y etsar entre 1.0 a 10.0
def validaderPeligrosidadDeLaEspecie():
     while True:
        peligrosidad_especie = float(input("Ingrese nivel de peligrosidad de la especie: \n"))
        if 1.0 < peligrosidad_especie < 10.0:
            return peligrosidad_especie
        else:
             print("Ingrese un número entre 1.0 y 10.0")
             
def agregarBicho():
      #nombre
      nombre = validarNombreDelaEspecie()
      #tamaño
      longitud = validarTamanioDeLaEspecie()
      #peligrosidad
      peligrosidad = validaderPeligrosidadDeLaEspecie()
      #el programa determina si es peligroso >7.0 son peligrosos
     
#Funcion encargada de inciar el programa :p normalemnte se llama "main"
def main():
    mostrarMenu()
    opcion_de_usuario = leerOpcion() #creamos una variable que contenga a la función leerOpcion() con la finalidad de asociar la opci+on seleccionada por el usuario con la opción del menú y llamar a la funcion que se usará en casa caso
    if opcion_de_usuario == "1":
            print("\nAGREGAR BICHO")
            agregarBicho()
    elif opcion_de_usuario == "2":
            print("BUSCAR BICHO")
    elif opcion_de_usuario == "3":
            print("ELIMINAR BICHO")
    elif opcion_de_usuario == "4":
            print("ACTUALIZAR ESTADOS")
    elif opcion_de_usuario == "5":
            print("MOSTRAR BICHOS")
    elif opcion_de_usuario == "6":
          print("SALIR")
    else:
        print("Opción inválida")

main()