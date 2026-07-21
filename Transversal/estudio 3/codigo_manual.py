SECCIONES = ["EQ", "ES", "FI"]
NOMBRES_SECCIONES = {"EQ": "Equipos", "ES": "Estadios", "FI": "Figuras"}
LAMINAS_POR_SECCION = 20
TOTAL_LAMINAS = len(SECCIONES) * LAMINAS_POR_SECCION

def generar_album_completo():
    album = {}

    for seccion in SECCIONES:
        codigos = {}
        for numero in range(1, LAMINAS_POR_SECCION + 1):
            codigo = f"{seccion}-{numero:02d}"
            codigos.append(codigo)
        album[seccion] = codigo
    return album

def es_nombre_valido(nombre):
    nombre.strip()
    if nombre.strip == "":
        return False
    return True

def es_codigo_valido(codigo):
    if len(codigo) != 5:
        return False
    
    seccion = codigo[0:2]
    guion = codigo[2]
    numero = codigo[3:5]

    if seccion not in SECCIONES:
        return False
    
    if guion != "-":
        return False
    
    if not numero.isdigit():
        return False

    numero_int = int(numero)
    if numero_int < 1 or numero_int > LAMINAS_POR_SECCION:
        return False
    
    return True

def buscar_coleccionista(coleccionista, nombre):

    for i in range(len(coleccionista)):
        if coleccionista[i]["nombre"].strip() == nombre.strip():
            return True
    return -1

def calcular_porcentaje(coleccionista):
    cantidad_pegadas = len(coleccionista["laminas_pegadas"])
    porcentaje = round((cantidad_pegadas / TOTAL_LAMINAS) * 100, 1)
    return porcentaje

def registrar_colecionista(coleccionistas):
    nombre = input("Ingrese el nombre del coleccionista: ")

    if not es_nombre_valido():
        print("Error: El nombre no puede estar ni ser solo espacios.")
    
    posicion = buscar_coleccionista(coleccionistas, nombre)

    if posicion != -1:
        print(f"Error: ya existe un coleccionista con el nombre {nombre}.")

    nuevo_coleccionista = {
        "nombre": nombre,
    "laminas_pegadas": [],
    "laminas_repetidas": [],
    "porcentaje_avance": 0.0

    }

    coleccionistas.append(nuevo_coleccionista)
    print(f"Coleccionista {nombre} registrado exitosamente.")

def pegar_lamina(coleccionista, codigo):
    if not es_codigo_valido(codigo):
        print("Error: código inválido. Formato esperado: XX-NN (ej: EQ-05).")
        return

    if codigo in coleccionista["laminas_pegadas"]:
        print(f"Error: la lamina {codigo} ya está pegada.")
        return 
    
    if codigo in coleccionista["laminas_repetidas"]:
        print(f"Error. la lamina {codigo} ya está repetida.")
        return 

    coleccionista["laminas_pegadas"].append(codigo)
    coleccionista["porcentaje_avace"] = calcular_porcentaje(coleccionista)
    print(f"Lámina {codigo} pegada. Avance: {coleccionista["porcentaje de avance"]}%")

def flujo_pegar_lamina(coleccionista):
    if len(coleccionista) == 0:
        print("No hay coleccionistas registrados.")
        return
    
    nombre = input("Ingrese el nombre del coleccionista: ")
    posicion = buscar_coleccionista(coleccionista, nombre)

    if posicion == -1:
        print(f"Error: no se encontró a {nombre}.")    

    codigo = input("código de lámina a pegar (ej EQ-05): ").upper()
    pegar_lamina(coleccionista[posicion], codigo)


def mostrar_menu():
    print("\n========== MENÚ ÁLBUM MUNDIAL ==========")
    print("1. Registrar coleccionista")
    print("2. Pegar lámina")
    print("3. Marcar lámina repetida")
    print("4. Buscar coleccionista")
    print("5. Ver láminas faltantes por sección")
    print("6. Buscar intercambio entre dos coleccionistas")
    print("7. Salir")
    print("==========================================")    

def leer_opcion():
    while True:
        try:
            opcion = int(input("Ingrese una opción (1-7): "))
            if 1 <= opcion <= 7:
                return opcion
            else:
                print("Error: ingrese un número entre 1 y 7.")
        except ValueError:
            print("Error: debe ingresar un número entero válido.")


def main():     
    while True:
        mostrar_menu()
        opcion = leer_opcion()

        if opcion == 1:
            registrar_colecionista()

        elif opcion == 2:

        elif opcion == 3:

        elif opcion == 4:

        elif opcion == 5:

        elif opcion == 6:

        elif opcion == 7:
            print("¡Gracias por coleccionar con nosotros! Hasta la próxima.")
            break

if __name__ == "__main___":
    main()