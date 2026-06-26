lista_estudiantes =[]

def validar_nombre():
    while True:
        nombre = input("Ingrese su nombre: ")
        if nombre.strip() == "":
            print("No es valido")
        else:
            return nombre
        
def validar_nota():
    while True:
        try:
            nota = float(input("Ingrese su nota: "))
            if nota < 1.0 or nota > 7.0:
                print("La nota debe ser entre 1.0 y 7.0")
            else:
                return nota
        except ValueError:
            print("Ingrese un numero entero")
        
def agregar_registro(lista):
    nombre_valido = validar_nombre()
    edad_valida = validar_edad()
    nota_valida = validar_nota()

    datos_registro ={
        "nombre": nombre_valido,
        "edad" : edad_valida,
        "nota": nota_valida
    }
    lista.append(datos_registro)
    print("El registro se guardo de forma exitosa")

    
def validar_edad():
    while True:
        try:
            edad = int(input("Ingrese su edad: "))
            if edad <= 0:
                print("Edad debe ser mayor a 0")
            else:
                return edad
        except ValueError:
            print("Ingrese un numero entero")



def eliminar_estudiante(lista, nombre_buscar):
    posicion = busca_estudiante(lista, nombre_buscar)
    if posicion != -1:
        lista.pop (posicion)
        print("Registro eliminado")
    else:
        print(f"El registro '{nombre_buscar}' no se encuentra")


def actualizar_datos(lista):
    for cada_registro in lista:
        if cada_registro ["nota"] > 4.0:
            cada_registro ["aprobado"] = True
        else:
            cada_registro ["aprobado"] = False


def busca_estudiante(lista, nombre_buscar):
    for cada_registro in lista:
        if cada_registro ["nombre"].lower == nombre_buscar.lower():
            print("Existe")
        indice_registro = lista.index(cada_registro)
        return indice_registro
    return -1
#falto () en .lower
    

def mostrar_estudiantes(lista):
    actualizar_datos(lista)
    print("==== lista de registro ===")
    for registro in lista:
        estado = "aprobado" if registro ["aprobado"] else "reprobado"
        print("nombre : {registro[nombre]}")
        print("edad: {registro[edad]}")
        print("nota: {registro[nota]}")
        print(f"estado: {estado}")
        #falto (f"nota: {registro['nota']}")

    
def mostrarmenu():
    print("1. Agregar Estudiante")
    print("2. Buscar Estudiante")
    print("3. Eliminar Estudiante")
    print("4. Actualizar Estados")
    print("5. Mostrar Estudiantes")
    print("6. Salir")
    


def iniciar_programa():
    while True:
        mostrarmenu()
        opcion_usuario = input("Ingrese su opcion:")

        if opcion_usuario == "1":
            agregar_registro(lista_estudiantes)

        elif opcion_usuario == "2":
            nombre_buscar = input("Ingrese el nombre que desea buscar: ")
            posicion = busca_estudiante(lista_estudiantes,nombre_buscar)
            if posicion != -1:
                print("Estudiante encontrado")
            else:
                print("El registro de {nombre_buscar} no se encuentra")

        elif opcion_usuario == "3":
            nombre_eliminar = input("Ingrese estudiante a eliminar: ")
            eliminar_estudiante(lista_estudiantes, nombre_eliminar)

        elif opcion_usuario == "4":
            actualizar_datos(lista_estudiantes)
            print("Estado actualizado")

        elif opcion_usuario == "5":
            mostrar_estudiantes(lista_estudiantes)

        elif opcion_usuario == "6":
            print("Gracias por usar el sistema. Vuelva Pronto")
            #falto break
        
                     
iniciar_programa()
            
    





       













