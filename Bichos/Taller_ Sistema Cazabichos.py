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

#RECORDAR: cuando tenga que válidar un número usar el try/except si o si owo
#Ahora validaremos el tamaño del bicho, debe ser mayor a 0
def validarTamanioDeLaEspecie():
     while True:
        try:
            longitud_especie = int(input("Ingrese tamaño de la especie: \n"))
            if longitud_especie <= 0:
                print("El tamaño del bicho debe ser mayor a 0.")
            else:
                return longitud_especie
        except ValueError:
            print("Ingrese un número válido")

#Es momento de validar la peligrosidad del bicho debe ser mayor a 0 y etsar entre 1.0 a 10.0
def validaderPeligrosidadDeLaEspecie():
     while True:
        try:
            peligrosidad_especie = float(input("Ingrese nivel de peligrosidad de la especie: \n"))
            if 1.0 < peligrosidad_especie < 10.0:
                return peligrosidad_especie
            else:
                print("Ingrese un número entre 1.0 y 10.0")
        except ValueError:
            print("Ingrese un número válido")

#Ahora vamos a registrar los bichos
def registrarEspecie(diccionario):
    lista_bichos.append(diccionario)
    print("El bicho fue registradro de forma exitosa.")
    return True

#Creamos una función que englobe a todos 
def agregarBicho():
    #nombre
    nombre = validarNombreDelaEspecie()
    #tamaño
    longitud = validarTamanioDeLaEspecie()
    #peligrosidad
    peligrosidad = validaderPeligrosidadDeLaEspecie()
    #el programa determina si es peligroso >7.0 son peligrosos

    #generamos un diccionario de acuerdo a la información solicitada x.x
    datos_de_la_especie = {
         "Nombre":nombre,
         "Tamaño (cm)":longitud,
         "Peligrosidad":peligrosidad,
         "Peligroso":False
    }
    #Usamos la función registrar especie, con la finalidad de ingresar el diccionario a la lista vacía del inicio
    registro = registrarEspecie(datos_de_la_especie)
    if registro == True:
        print("El registro se ha realizado de forma exitosa.")
        return True
    else:
        print("Ha ocurrido un error inesperado.")
        return False

#Buscar un bicho dentro de la lista de diccionarios
def buscarBichoPorNombre(nombre_a_buscar):
    for cada_bicho in lista_bichos:
        if cada_bicho["nombre_especie"] == nombre_a_buscar:
            print("Existe")
            indice = lista_bichos.index(cada_bicho)
            return indice  
         
#Eliminar bicho
def eliminarBivhoPorNombre(nombre):
    indice_del_bischo_a_buscar = buscarBichoPorNombre(nombre)
    if indice_del_bischo_a_buscar is not None:
        if lista_bichos.pop(indice_del_bischo_a_buscar):
            return True
        else:
            return False

#Actualidad la peligrosidad d ela especie
def actualizarPeligrosidad():
    for cada_bicho in lista_bichos:
        if cada_bicho["Peligrosidad"] >= 7.0:
            cada_bicho["Peligroso"] == True
 
#Funcion encargada de inciar el programa :p normalemnte se llama "main"
def main():
    while True:
        mostrarMenu()
        opcion_de_usuario = leerOpcion() #creamos una variable que contenga a la función leerOpcion() con la finalidad de asociar la opci+on seleccionada por el usuario con la opción del menú y llamar a la funcion que se usará en casa caso
        if opcion_de_usuario == "1":
            print("\n========== AGREGAR BICHO ==========")
            agregarBicho()
        elif opcion_de_usuario == "2":
            print("\n========== BUSCAR BICHO ==========")
            while True:
                nombre_a_buscar = input("Ingrese el nombre del bicho a busar: \n")
                if " " in nombre_a_buscar or len(nombre_a_buscar) < 0:
                    print("Ingrese un nombre válido")
                else:
                    break
            indice_del_bicho = buscarBichoPorNombre(nombre_a_buscar)
            if indice_del_bicho is not None:
                print("Bicho encontrado")
            else:
                print("No existe")

        elif opcion_de_usuario == "3":
            print("\n========== ELIMINAR BICHO ==========")
            while True:
                nombre_a_eliminar = input("Ingrese el nombre del bicho a busar: \n")
                if " " in nombre_a_eliminar or len(nombre_a_eliminar) < 0:
                    print("Ingrese un nombre válido")
                else:
                    break
            fue_eliminado = eliminarBivhoPorNombre(nombre_a_eliminar)
            if fue_eliminado == True:
                print("Ha sido eliminado")
            else:
                print("No se úedo eliminar")
                
        elif opcion_de_usuario == "4":
            print("\n========== ACTUALIZAR ESTADOS ==========")
            actualizarPeligrosidad()
        elif opcion_de_usuario == "5":
            print("\n========== MOSTRAR BICHOS ==========")
            print(lista_bichos)
        elif opcion_de_usuario == "6":
            print("\n========== SALIR ==========")
            print("Gracias por usar el Cazabichos. ¡Hasta la próxima expedición!")
            break
        else:
            print("Opción inválida")

main()