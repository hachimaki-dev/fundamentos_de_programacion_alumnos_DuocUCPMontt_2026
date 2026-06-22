#Ejercicio 1 — Sistema de Gestión de una Biblioteca
#Contexto: Una biblioteca necesita llevar registro de sus libros.
#Datos que maneja el sistema
#Campo Qué representa Restricciones de validación
todos_los_libros=[]

def mostrar_menu():
    print("\n========= MENÚ PRINCIPAL ==========")
    print("1. Agregar libro")
    print("2. Buscar libro")
    print("3. Eliminar libro")
    print("4. Actualizar disponibilidad")
    print("5. Mostrar libros")
    print("6. Salir")
    print("7. Prueba")
    print("=====================================")
def leer_opcion_usuario_menu():
    while True:
        opcion_ingresada = input("Ingrese su opción: ")
        if opcion_ingresada in ["1", "2", "3", "4", "5", "6", "7"]:
            return opcion_ingresada
        else:
            print("Opcion invalida, vuelva a intentar")

def validar_nombre_libro():
    titulo_libro = input("Ingrese el título del libro: ").strip()
    if len(titulo_libro)<=0:
        print("El título del libro no es válido")
    else:
        return titulo_libro
def validar_autor_libro():
    autor_libro = input("Ingrese el autor del libro: ").strip()
    if len(autor_libro)<=0:
        print("El nombre del autor no es válido")
    else:
        return autor_libro
def cantidad_ejemplares_libro():
    while True:
        try:
            cantidad_ejemplares=int(input("Ingrese la cantidad de ejemplares del libro: "))
            if cantidad_ejemplares<0:
                print("La cantidad de ejemplares no puede ser negativa, por favor ingrese un número válido")
            else:
                return cantidad_ejemplares
        except ValueError:
            print("Valor inválido, por favor ingrese un número entero")
def verificar_disponibilidad():
    disponibilidad = False
    return disponibilidad

def agregar_libro():
    titulo=validar_nombre_libro()
    autor=validar_autor_libro()
    ejemplares=cantidad_ejemplares_libro()
    disponibilidad=verificar_disponibilidad()

    print(f"El título del libro es {titulo}, su autor es {autor}, la cantidad de ejemplares es {ejemplares} y su disponibilidad es: {disponibilidad}")
    datos_del_libro={
        "titulo": titulo,
        "autor": autor,
        "ejemplares": ejemplares,
        "disponibilidad": disponibilidad
    }
    todos_los_libros.append(datos_del_libro)
def buscar_libro_por_titulo(titulo_a_buscar):
    for cada_libro in todos_los_libros:
        if cada_libro["titulo"] == titulo_a_buscar:
            print("Existe el libro")
            index_libro=todos_los_libros.index(cada_libro)
            return index_libro
    print("No existe el libro")
    return -1
def eliminar_libro_por_nombre(titulo_a_buscar):
    indice_nombre_libro=buscar_libro_por_titulo(titulo_a_buscar)
    if indice_nombre_libro!=-1:
        todos_los_libros.pop(indice_nombre_libro)
        return True
def actualizar_disponibilidad():
    for cada_libro in todos_los_libros:
        if cada_libro["disponibilidad"]>0:
            cada_libro["disponibilidad"]=True
        else:
            cada_libro["disponibilidad"]=False
def mostrar_todos_los_libros():
    print(todos_los_libros)
def insertar_datos_de_prueba():
    todos_los_libros.append({
        "titulo": "mariposa",
        "autor": "Renato",
        "ejemplares": 2,
        "disponibilidad": False
    })

    todos_los_libros.append({
        "titulo": "gusano",
        "autor": "Hugo",
        "ejemplares": 8,
        "disponibilidad": False
    })

    todos_los_libros.append({
        "titulo": "garrapata",
        "autor": "David",
        "ejemplares": 9,
        "disponibilidad": False
    })

def iniciar_programa():
    while True:
        mostrar_menu()
        opcion_menu_usuario_validada=leer_opcion_usuario_menu()

        if opcion_menu_usuario_validada=="1":
            agregar_libro()
        elif opcion_menu_usuario_validada=="2":
            libro_a_buscar=input("Ingrese el titulo del libro a buscar: \n")
            indice_encontrado=buscar_libro_por_titulo(libro_a_buscar)

            if indice_encontrado is not None:
                print("Lo encontramos")
                print(f"Titulo: {todos_los_libros[indice_encontrado]}")
                print(f"Autor: {todos_los_libros[indice_encontrado]}")
                print(f"Ejemplares: {todos_los_libros[indice_encontrado]}")
                print(f"Disponibilidad: {todos_los_libros[indice_encontrado]}")
            else:
                print("No encontramos datos del libro")
        elif opcion_menu_usuario_validada=="3":
            nombre_del_libro_a_eliminar=input("Ingrese el nombre del libro a eliminar: ")
            se_elimino=eliminar_libro_por_nombre(nombre_del_libro_a_eliminar)
            if se_elimino is not None:
                print("Se elimino con exito")
            else:
                print("No se puede eliminar algo que no existe")
        elif opcion_menu_usuario_validada=="4":
            actualizar_disponibilidad()
        elif opcion_menu_usuario_validada=="5":
            mostrar_todos_los_libros()
        elif opcion_menu_usuario_validada=="6":
            print("Salimos")
            break
        elif opcion_menu_usuario_validada=="7":
            insertar_datos_de_prueba()
        else:
            print("Opcion no valida")

iniciar_programa()