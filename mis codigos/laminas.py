# ============================================
# Sistema de gestión de colección de láminas - Álbum del Mundial
# ============================================
#
# DIFERENCIA CLAVE respecto a AniStream:
# - Ahí teníamos DOS DICCIONARIOS unidos por un código (acceso por clave).
# - Acá tenemos UNA LISTA de diccionarios (coleccionistas), y cada
#   diccionario tiene, a su vez, DOS LISTAS propias adentro
#   (laminas_pegadas, laminas_repetidas).
# - Por eso, para "buscar" ya no hacemos "codigo in diccionario",
#   sino que recorremos la lista comparando el campo 'nombre'.

coleccionistas = []  # lista vacía al iniciar el programa

SECCIONES = [('Equipos', 'EQ'), ('Estadios', 'ES'), ('Figuras', 'FI')]
LAMINAS_POR_SECCION = 20
TOTAL_LAMINAS = LAMINAS_POR_SECCION * len(SECCIONES)  # 60


# ============================================
# MENÚ: dos funciones separadas (regla de arquitectura del enunciado)
# ============================================
def mostrar_menu():
    # No recibe nada, no retorna nada. Solo imprime.
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
    # Lee y retorna la opción. Fuerza reintento con el patrón de
    # bandera + while que ya conoces, hasta obtener un entero válido.
    opcion_valida = False
    while not opcion_valida:
        try:
            opcion = int(input("Seleccione una opción: "))
            opcion_valida = True
        except ValueError:
            print("Debe ingresar un número entero válido.")
    return opcion


# ============================================
# VALIDACIONES PURAS (solo True/False, sin prints)
# ============================================
def validar_nombre(nombre):
    return bool(nombre.strip())


def validar_formato_codigo(codigo):
    # Formato esperado: 2 letras + guion + 2 números. Ej: "EQ-05"
    if len(codigo) != 5:
        return False
    seccion = codigo[0:2]
    guion = codigo[2]
    numero = codigo[3:5]

    if seccion not in ('EQ', 'ES', 'FI'):
        return False
    if guion != '-':
        return False
    if not numero.isdigit():
        return False
    if not (1 <= int(numero) <= LAMINAS_POR_SECCION):
        return False
    return True


# ============================================
# HELPERS internos
# ============================================
def calcular_porcentaje(coleccionista):
    cantidad_pegadas = len(coleccionista["laminas_pegadas"])
    return round((cantidad_pegadas / TOTAL_LAMINAS) * 100, 1)


# ============================================
# OPCIÓN 1: Registrar coleccionista
# ============================================
def registrar_coleccionista(lista_coleccionistas):
    nombre = input("Nombre del coleccionista: ")

    # La validación es "pura" (sin prints); el mensaje se muestra ACÁ.
    if not validar_nombre(nombre):
        print("El nombre no puede estar vacío ni ser solo espacios.")
        return

    nuevo = {
        "nombre": nombre,
        "laminas_pegadas": [],      # lista vacía al registrar
        "laminas_repetidas": [],    # lista vacía al registrar
        "porcentaje_avance": 0
    }
    lista_coleccionistas.append(nuevo)
    print(f"Coleccionista '{nombre}' registrado con éxito.")


# ============================================
# OPCIÓN 4: Buscar coleccionista (retorna índice o -1)
# ============================================
def buscar_coleccionista(lista_coleccionistas, nombre):
    for indice, coleccionista in enumerate(lista_coleccionistas):
        if coleccionista["nombre"] == nombre:
            return indice
    return -1


# ============================================
# OPCIÓN 2: Pegar lámina
# ============================================
def pegar_lamina(coleccionista, codigo):
    if not validar_formato_codigo(codigo):
        return False
    if codigo in coleccionista["laminas_pegadas"]:
        return False

    coleccionista["laminas_pegadas"].append(codigo)
    coleccionista["porcentaje_avance"] = calcular_porcentaje(coleccionista)
    return True


# ============================================
# OPCIÓN 3: Marcar lámina repetida
# ============================================
def marcar_lamina_repetida(coleccionista, codigo):
    if not validar_formato_codigo(codigo):
        return False
    # Regla de negocio nueva: no puede estar ya pegada.
    if codigo in coleccionista["laminas_pegadas"]:
        return False
    if codigo in coleccionista["laminas_repetidas"]:
        return False

    coleccionista["laminas_repetidas"].append(codigo)
    return True


# ============================================
# OPCIÓN 5: Ver láminas faltantes por sección
# ============================================
def ver_faltantes(coleccionista):
    print(f"\n=== AVANCE DE {coleccionista['nombre']} ===")
    print(f"Avance total: {coleccionista['porcentaje_avance']}%\n")

    for nombre_seccion, prefijo in SECCIONES:
        faltantes = []
        for numero in range(1, LAMINAS_POR_SECCION + 1):
            codigo = f"{prefijo}-{numero:02d}"
            if codigo not in coleccionista["laminas_pegadas"]:
                faltantes.append(codigo)

        if faltantes:
            print(f"Sección {nombre_seccion} — faltan {len(faltantes)} de {LAMINAS_POR_SECCION}:")
            print("  " + ", ".join(faltantes))
        else:
            print(f"Sección {nombre_seccion} — completa")
        print()


# ============================================
# OPCIÓN 6: Buscar intercambio entre dos coleccionistas
# ============================================
def buscar_intercambio(coleccionista_1, coleccionista_2):
    # Lo que el 1 podría darle al 2: sus repetidas que al 2 le faltan.
    c1_puede_dar = []
    for codigo in coleccionista_1["laminas_repetidas"]:
        if codigo not in coleccionista_2["laminas_pegadas"]:
            c1_puede_dar.append(codigo)

    # Lo que el 2 podría darle al 1: sus repetidas que al 1 le faltan.
    c2_puede_dar = []
    for codigo in coleccionista_2["laminas_repetidas"]:
        if codigo not in coleccionista_1["laminas_pegadas"]:
            c2_puede_dar.append(codigo)

    return c1_puede_dar, c2_puede_dar


# ============================================
# PROGRAMA PRINCIPAL
# ============================================
def menu():
    while True:
        mostrar_menu()
        opcion = leer_opcion()

        if opcion == 1:
            registrar_coleccionista(coleccionistas)

        elif opcion == 2:
            nombre = input("Nombre del coleccionista: ")
            indice = buscar_coleccionista(coleccionistas, nombre)
            if indice == -1:
                print("Coleccionista no encontrado.")
            else:
                codigo = input("Código de la lámina a pegar (ej: EQ-05): ").upper()
                if pegar_lamina(coleccionistas[indice], codigo):
                    avance = coleccionistas[indice]["porcentaje_avance"]
                    print(f"Lámina pegada con éxito. Avance: {avance}%")
                else:
                    print("No se pudo pegar la lámina (código inválido o ya estaba pegada).")

        elif opcion == 3:
            nombre = input("Nombre del coleccionista: ")
            indice = buscar_coleccionista(coleccionistas, nombre)
            if indice == -1:
                print("Coleccionista no encontrado.")
            else:
                codigo = input("Código de la lámina repetida (ej: ES-14): ").upper()
                if marcar_lamina_repetida(coleccionistas[indice], codigo):
                    print("Lámina marcada como repetida con éxito.")
                else:
                    print("No se pudo marcar (código inválido, ya pegada, o ya estaba repetida).")

        elif opcion == 4:
            nombre = input("Nombre a buscar: ")
            indice = buscar_coleccionista(coleccionistas, nombre)
            if indice == -1:
                print("Coleccionista no encontrado.")
            else:
                print(f"Encontrado en la posición {indice}: {coleccionistas[indice]}")

        elif opcion == 5:
            nombre = input("Nombre del coleccionista: ")
            indice = buscar_coleccionista(coleccionistas, nombre)
            if indice == -1:
                print("Coleccionista no encontrado.")
            else:
                ver_faltantes(coleccionistas[indice])

        elif opcion == 6:
            nombre1 = input("Nombre del primer coleccionista: ")
            nombre2 = input("Nombre del segundo coleccionista: ")
            indice1 = buscar_coleccionista(coleccionistas, nombre1)
            indice2 = buscar_coleccionista(coleccionistas, nombre2)

            if indice1 == -1 or indice2 == -1:
                print("Uno o ambos coleccionistas no fueron encontrados.")
            elif nombre1 == nombre2:
                print("Debes ingresar dos coleccionistas distintos.")
            else:
                c1_da, c2_da = buscar_intercambio(coleccionistas[indice1], coleccionistas[indice2])
                if not c1_da and not c2_da:
                    print(f"No hay intercambios posibles entre '{nombre1}' y '{nombre2}'.")
                else:
                    if c1_da:
                        print(f"{nombre1} podría darle a {nombre2}: {', '.join(c1_da)}")
                    if c2_da:
                        print(f"{nombre2} podría darle a {nombre1}: {', '.join(c2_da)}")

        elif opcion == 7:
            print("¡Gracias por coleccionar con nosotros! Hasta la próxima.")
            break

        else:
            print("Debe seleccionar una opción válida")


if __name__ == "__main__":
    menu()