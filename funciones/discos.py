# ============================================================
# VINYL EXCHANGE - Solución completa de referencia
# ============================================================
# Úsala para ENTENDER el razonamiento, no para copiar/pegar en
# el ejercicio de láminas. Los nombres de campos y las reglas
# de negocio son distintas allá -- tendrás que pensar de nuevo
# cada paso, no solo cambiar palabras.
# ============================================================

GENEROS = ["RO", "JA", "SO"]
DISCOS_POR_GENERO = 15
TOTAL_DISCOS = len(GENEROS) * DISCOS_POR_GENERO  # 45

coleccionistas = []  # lista general, vacía al iniciar


# ------------------------------------------------------------
# CATÁLOGO COMPLETO
# ------------------------------------------------------------
def generar_catalogo_completo():
    """
    Devuelve algo como:
    {"RO": ["RO-01", "RO-02", ..., "RO-15"],
     "JA": ["JA-01", ..., "JA-15"],
     "SO": ["SO-01", ..., "SO-15"]}
    """
    catalogo = {}
    for genero in GENEROS:
        codigos = []
        for numero in range(1, DISCOS_POR_GENERO + 1):
            # :02d rellena con un 0 a la izquierda si el número tiene 1 dígito
            # (1 -> "01", 15 -> "15")
            codigo = f"{genero}-{numero:02d}"
            codigos.append(codigo)
        catalogo[genero] = codigos
    return catalogo


# ------------------------------------------------------------
# VALIDACIÓN DE CÓDIGO
# ------------------------------------------------------------
def es_codigo_valido(codigo):
    # 1. Largo total: 2 letras + guion + 2 números = 5 caracteres
    if len(codigo) != 5:
        return False

    prefijo = codigo[0:2]
    guion = codigo[2]
    numero_str = codigo[3:5]

    # 2. El prefijo debe ser uno de los géneros válidos
    if prefijo not in GENEROS:
        return False

    # 3. El separador debe ser un guion
    if guion != "-":
        return False

    # 4. Los últimos 2 caracteres deben ser dígitos
    if not numero_str.isdigit():
        return False

    # 5. Convertir a entero y revisar el rango 1-15
    numero = int(numero_str)
    if numero < 1 or numero > DISCOS_POR_GENERO:
        return False

    return True


# ------------------------------------------------------------
# BÚSQUEDA DE COLECCIONISTA
# ------------------------------------------------------------
def buscar_coleccionista(lista_coleccionistas, nombre):
    for i in range(len(lista_coleccionistas)):
        if lista_coleccionistas[i]["nombre"] == nombre:
            return i
    return -1


# ------------------------------------------------------------
# PORCENTAJE
# ------------------------------------------------------------
def calcular_porcentaje(coleccionista):
    cantidad = len(coleccionista["discos_coleccion"])
    return round((cantidad / TOTAL_DISCOS) * 100, 1)


# ------------------------------------------------------------
# OPCIÓN 1: REGISTRAR
# ------------------------------------------------------------
def es_nombre_valido(nombre):
    # .strip() quita espacios al inicio/final; si queda vacío, no era válido
    return len(nombre.strip()) > 0


def registrar_coleccionista(lista_coleccionistas):
    nombre = input("Nombre del coleccionista: ")

    if not es_nombre_valido(nombre):
        print("El nombre no puede estar vacío o ser solo espacios.")
        return

    nuevo = {
        "nombre": nombre,
        "discos_coleccion": [],
        "discos_duplicados": [],
        "porcentaje_coleccion": 0.0
    }
    lista_coleccionistas.append(nuevo)
    print(f"Coleccionista '{nombre}' registrado con éxito.")


# ------------------------------------------------------------
# OPCIÓN 2: AGREGAR DISCO A LA COLECCIÓN
# ------------------------------------------------------------
def agregar_disco_a_coleccion(coleccionista, codigo):
    if not es_codigo_valido(codigo):
        print("Código de disco inválido.")
        return

    if codigo in coleccionista["discos_coleccion"]:
        print("Este disco ya está en la colección.")
        return

    # Regla de negocio: si estaba duplicado, se "asciende" a colección
    if codigo in coleccionista["discos_duplicados"]:
        coleccionista["discos_duplicados"].remove(codigo)
        print(f"(el disco {codigo} estaba duplicado, se movió a la colección)")

    coleccionista["discos_coleccion"].append(codigo)
    coleccionista["porcentaje_coleccion"] = calcular_porcentaje(coleccionista)
    print(f"Disco {codigo} agregado. Avance: {coleccionista['porcentaje_coleccion']}%")


# ------------------------------------------------------------
# OPCIÓN 3: MARCAR DUPLICADO
# ------------------------------------------------------------
def marcar_disco_duplicado(coleccionista, codigo):
    if not es_codigo_valido(codigo):
        print("Código de disco inválido.")
        return

    if codigo in coleccionista["discos_coleccion"]:
        print("Este disco ya está en tu colección, no tiene sentido marcarlo duplicado.")
        return

    if codigo in coleccionista["discos_duplicados"]:
        print("Este disco ya estaba marcado como duplicado.")
        return

    coleccionista["discos_duplicados"].append(codigo)
    print(f"Disco {codigo} marcado como duplicado.")


# ------------------------------------------------------------
# OPCIÓN 5: DISCOS FALTANTES POR GÉNERO
# ------------------------------------------------------------
def discos_faltantes(coleccionista):
    catalogo = generar_catalogo_completo()
    faltantes = {}
    for genero in GENEROS:
        faltantes_genero = []
        for codigo in catalogo[genero]:
            if codigo not in coleccionista["discos_coleccion"]:
                faltantes_genero.append(codigo)
        faltantes[genero] = faltantes_genero
    return faltantes


def mostrar_faltantes(coleccionista):
    faltantes = discos_faltantes(coleccionista)
    print(f"\n=== AVANCE DE {coleccionista['nombre']} ===")
    print(f"Avance total: {coleccionista['porcentaje_coleccion']}%\n")

    for genero in GENEROS:
        cantidad_faltante = len(faltantes[genero])
        if cantidad_faltante == 0:
            print(f"Género {genero} — completo")
        else:
            print(f"Género {genero} — faltan {cantidad_faltante} de {DISCOS_POR_GENERO}:")
            print("  " + ", ".join(faltantes[genero]))
    print()


# ------------------------------------------------------------
# OPCIÓN 6: INTERCAMBIO
# ------------------------------------------------------------
def que_le_falta_a(receptor, ofertante):
    """Discos duplicados de 'ofertante' que le sirven a 'receptor'."""
    posibles = []
    for codigo in ofertante["discos_duplicados"]:
        if codigo not in receptor["discos_coleccion"]:
            posibles.append(codigo)
    return posibles


def buscar_intercambio(coleccionista_a, coleccionista_b):
    de_a_hacia_b = que_le_falta_a(coleccionista_b, coleccionista_a)
    de_b_hacia_a = que_le_falta_a(coleccionista_a, coleccionista_b)

    if len(de_a_hacia_b) == 0 and len(de_b_hacia_a) == 0:
        print(f"No hay intercambios posibles entre '{coleccionista_a['nombre']}' "
              f"y '{coleccionista_b['nombre']}'.")
        return

    if len(de_a_hacia_b) > 0:
        print(f"{coleccionista_a['nombre']} le puede ofrecer a "
              f"{coleccionista_b['nombre']}: {', '.join(de_a_hacia_b)}")

    if len(de_b_hacia_a) > 0:
        print(f"{coleccionista_b['nombre']} le puede ofrecer a "
              f"{coleccionista_a['nombre']}: {', '.join(de_b_hacia_a)}")


# ------------------------------------------------------------
# MENÚ
# ------------------------------------------------------------
def mostrar_menu():
    print("========== VINYL EXCHANGE ==========")
    print("1. Registrar coleccionista")
    print("2. Agregar disco a la colección")
    print("3. Marcar disco duplicado")
    print("4. Buscar coleccionista")
    print("5. Ver discos faltantes por género")
    print("6. Buscar intercambio entre dos coleccionistas")
    print("7. Salir")
    print("=====================================")


def leer_opcion():
    try:
        return int(input("Selecciona una opción: "))
    except ValueError:
        print("Por favor ingresa un número válido.")
        return None  # usamos None para distinguir "opción inválida" de una opción real


# ------------------------------------------------------------
# PROGRAMA PRINCIPAL
# ------------------------------------------------------------
def main():
    opcion = 0
    while opcion != 7:
        mostrar_menu()
        opcion = leer_opcion()

        if opcion is None:
            continue  # ya se imprimió el error dentro de leer_opcion

        if opcion == 1:
            registrar_coleccionista(coleccionistas)

        elif opcion == 2:
            nombre = input("Nombre del coleccionista: ")
            pos = buscar_coleccionista(coleccionistas, nombre)
            if pos == -1:
                print("No existe un coleccionista con ese nombre.")
            else:
                codigo = input("Código del disco a agregar: ").upper()
                agregar_disco_a_coleccion(coleccionistas[pos], codigo)

        elif opcion == 3:
            nombre = input("Nombre del coleccionista: ")
            pos = buscar_coleccionista(coleccionistas, nombre)
            if pos == -1:
                print("No existe un coleccionista con ese nombre.")
            else:
                codigo = input("Código del disco duplicado: ").upper()
                marcar_disco_duplicado(coleccionistas[pos], codigo)

        elif opcion == 4:
            nombre = input("Nombre a buscar: ")
            pos = buscar_coleccionista(coleccionistas, nombre)
            if pos == -1:
                print("No se encontró ningún coleccionista con ese nombre.")
            else:
                print(f"Encontrado en la posición {pos}: {coleccionistas[pos]}")

        elif opcion == 5:
            nombre = input("Nombre del coleccionista: ")
            pos = buscar_coleccionista(coleccionistas, nombre)
            if pos == -1:
                print("No existe un coleccionista con ese nombre.")
            else:
                mostrar_faltantes(coleccionistas[pos])

        elif opcion == 6:
            nombre_a = input("Nombre del primer coleccionista: ")
            nombre_b = input("Nombre del segundo coleccionista: ")

            if nombre_a == nombre_b:
                print("Debes ingresar dos coleccionistas distintos.")
                continue

            pos_a = buscar_coleccionista(coleccionistas, nombre_a)
            pos_b = buscar_coleccionista(coleccionistas, nombre_b)

            if pos_a == -1 or pos_b == -1:
                print("Uno o ambos coleccionistas no existen.")
            else:
                buscar_intercambio(coleccionistas[pos_a], coleccionistas[pos_b])

        elif opcion == 7:
            print("¡Que sigan girando esos discos! Hasta la próxima.")

        else:
            print("Opción inválida, intenta nuevamente.")


if __name__ == "__main__":
    main()