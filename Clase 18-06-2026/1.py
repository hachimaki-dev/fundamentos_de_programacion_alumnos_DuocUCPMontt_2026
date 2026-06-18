#Ejercicio 1 — Sistema de Gestión de una Biblioteca
#Contexto: Una biblioteca necesita llevar registro de sus libros.
#Datos que maneja el sistema
#Campo Qué representa Restricciones de validación
todos_los_libros=[]

def mostrar_menu():
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Agregar libro")
    print("2. Buscar libro")
    print("3. Eliminar libro")
    print("4. Actualizar disponibilidad")
    print("5. Mostrar libros")
    print("6. Salir")
    print("=====================================")

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
            if cantidad_ejemplares>=0:
                print("La cantidad de ejemplares no puede ser negativa, por favor ingrese un número válido")
            else:
                return cantidad_ejemplares
        except ValueError:
            print("Valor inválido, por favor ingrese un número entero")
def 

def agregar_libro():
    titulo=validar_nombre_libro()
    autor=validar_autor_libro()
    ejemplares=cantidad_ejemplares_libro()
