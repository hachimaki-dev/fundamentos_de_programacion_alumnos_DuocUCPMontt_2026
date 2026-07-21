estudiantes = []
def validar_numero_mayor_a_0(numero):
    try:
        numero = int(numero)

        if numero > 0:
            return True
        else:
            return False
    except ValueError:
        return False

def validar_nombre_estudiante(nombre):
    return nombre.strip()

def validar_nota_estudiante(nota):
    if validar_numero_mayor_a_0(nota):
        nota = int(nota)

        if 1 <= nota <= 100:
            return True
        else:
            return False

def validar_aprobado(nota):
    if nota >= 60:
        return True
    return False


while True:
    cantidad_estudiantes = input("Ingrese la cantidad de estudiantes a calificar: ")
    if not validar_numero_mayor_a_0(cantidad_estudiantes):
        print("Ingrese un número entero positivo mayor a 0.")
    else:
        cantidad_estudiantes = int(cantidad_estudiantes)
        break

contador = 1

while True:

    while True:
        nombre_del_estudiante = input(f"Ingrese el nombre del estudiante N°{contador}: ")
        if not validar_nombre_estudiante(nombre_del_estudiante):
            print("El nombre del estudiante no puede estar vació.")
        else:
            break
    while True:
        nota_del_estudiante = input(f"Ingrese la nota del estudiante N°{contador}: ")
        if not validar_numero_mayor_a_0(nota_del_estudiante):
            print("Ingrese un número entero positivo mayor a 0.")
            
        elif not validar_nota_estudiante(nota_del_estudiante):
            print("Ingrese un nota entre 1 y el 100.")
        
        else:
            estado_del_estudiante = validar_aprobado(nota_del_estudiante)
            break

    estudiante = {
        "nombre": nombre_del_estudiante,
        "nota": nota_del_estudiante,
        "estado": estado_del_estudiante
    }

    estudiantes.append(estudiante)
    contador += 1

    if contador > cantidad_estudiantes:
        break


