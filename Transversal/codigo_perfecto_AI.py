# =============================================================================
# CONFIGURACIÓN GLOBAL
# =============================================================================
SECCIONES = ["EQ", "ES", "FI"]
NOMBRES_SECCIONES = {"EQ": "Equipos", "ES": "Estadios", "FI": "Figuras"}
LAMINAS_POR_SECCION = 20
TOTAL_LAMINAS = 60

# =============================================================================
# FUNCIONES DE VALIDACIÓN Y BÚSQUEDA
# =============================================================================
def es_codigo_valido(codigo):
    if len(codigo) != 5 or codigo[2] != "-":
        return False
        
    seccion = codigo[0:2]
    numero_str = codigo[3:5]
    
    if seccion not in SECCIONES or not numero_str.isdigit():
        return False
        
    numero = int(numero_str)
    return 1 <= numero <= LAMINAS_POR_SECCION

def buscar_coleccionista(coleccionistas, nombre):
    for coleccionista in coleccionistas:
        if coleccionista["nombre"] == nombre:
            return coleccionista
    return None

# =============================================================================
# OPCIONES DEL MENÚ
# =============================================================================
def registrar_coleccionista(coleccionistas):
    print("\n--- Registrar Coleccionista ---")
    nombre = input("Ingrese el nombre del coleccionista: ").strip()
    
    if nombre == "":
        print("Error: el nombre no puede estar vacío.")
        return

    if buscar_coleccionista(coleccionistas, nombre) is not None:
        print(f"Error: ya existe un coleccionista con el nombre '{nombre}'.")
        return

    nuevo_coleccionista = {
        "nombre": nombre,
        "laminas_pegadas": [],
        "laminas_repetidas": [],
        "porcentaje_avance": 0.0
    }
    coleccionistas.append(nuevo_coleccionista)
    print(f"Coleccionista '{nombre}' registrado exitosamente.")

def pegar_lamina(coleccionistas):
    print("\n--- Pegar Lámina ---")
    if len(coleccionistas) == 0:
        print("No hay coleccionistas registrados.")
        return

    nombre = input("Nombre del coleccionista: ")
    coleccionista = buscar_coleccionista(coleccionistas, nombre)
    if coleccionista is None:
        print(f"Error: no se encontró a '{nombre}'.")
        return

    codigo = input("Código de lámina a pegar (ej: EQ-05): ").upper()
    if not es_codigo_valido(codigo):
        print("Error: código inválido. Formato esperado: XX-NN.")
        return

    if codigo in coleccionista["laminas_pegadas"]:
        print(f"Error: la lámina {codigo} ya está pegada.")
        return

    if codigo in coleccionista["laminas_repetidas"]:
        print(f"Error: {codigo} está en repetidas. Quítala de ahí primero.")
        return

    coleccionista["laminas_pegadas"].append(codigo)
    cantidad_pegadas = len(coleccionista["laminas_pegadas"])
    coleccionista["porcentaje_avance"] = round((cantidad_pegadas / TOTAL_LAMINAS) * 100, 1)
    print(f"Lámina {codigo} pegada. Avance: {coleccionista['porcentaje_avance']}%")

def marcar_lamina_repetida(coleccionistas):
    print("\n--- Marcar Lámina Repetida ---")
    if len(coleccionistas) == 0:
        print("No hay coleccionistas registrados.")
        return

    nombre = input("Nombre del coleccionista: ")
    coleccionista = buscar_coleccionista(coleccionistas, nombre)
    if coleccionista is None:
        print(f"Error: no se encontró a '{nombre}'.")
        return

    codigo = input("Código de lámina repetida (ej: FI-10): ").upper()
    if not es_codigo_valido(codigo):
        print("Error: código inválido. Formato esperado: XX-NN.")
        return

    if codigo in coleccionista["laminas_pegadas"]:
        print(f"Error: {codigo} ya está pegada. No puede ser repetida.")
        return

    if codigo in coleccionista["laminas_repetidas"]:
        print(f"Error: {codigo} ya está marcada como repetida.")
        return

    coleccionista["laminas_repetidas"].append(codigo)
    print(f"Lámina {codigo} marcada como repetida.")

def mostrar_coleccionista(coleccionistas):
    print("\n--- Buscar Coleccionista ---")
    if len(coleccionistas) == 0:
        print("No hay coleccionistas registrados.")
        return

    nombre = input("Nombre a buscar: ")
    coleccionista = buscar_coleccionista(coleccionistas, nombre)
    if coleccionista is None:
        print(f"No se encontró a '{nombre}'.")
        return

    print(f"\nDatos de {coleccionista['nombre']}:")
    print(f"  Avance: {coleccionista['porcentaje_avance']}%")
    
    pegadas = ", ".join(coleccionista["laminas_pegadas"])
    if pegadas == "":
        pegadas = "(ninguna)"
    print(f"  Pegadas ({len(coleccionista['laminas_pegadas'])}): {pegadas}")

    repetidas = ", ".join(coleccionista["laminas_repetidas"])
    if repetidas == "":
        repetidas = "(ninguna)"
    print(f"  Repetidas ({len(coleccionista['laminas_repetidas'])}): {repetidas}")

def ver_laminas_faltantes(coleccionistas):
    print("\n--- Ver Láminas Faltantes por Sección ---")
    if len(coleccionistas) == 0:
        print("No hay coleccionistas registrados.")
        return

    nombre = input("Nombre del coleccionista: ")
    coleccionista = buscar_coleccionista(coleccionistas, nombre)
    if coleccionista is None:
        print(f"Error: no se encontró a '{nombre}'.")
        return

    print(f"\n=== AVANCE DE {coleccionista['nombre']} ===")
    print(f"Avance total: {coleccionista['porcentaje_avance']}%\n")

    for seccion in SECCIONES:
        laminas_faltantes = []
        for numero in range(1, LAMINAS_POR_SECCION + 1):
            codigo = f"{seccion}-{numero:02d}"
            if codigo not in coleccionista["laminas_pegadas"]:
                laminas_faltantes.append(codigo)

        nombre_seccion = NOMBRES_SECCIONES[seccion]
        if len(laminas_faltantes) == 0:
            print(f"Sección {nombre_seccion} — completa")
        else:
            texto_faltantes = ", ".join(laminas_faltantes)
            print(f"Sección {nombre_seccion} — faltan {len(laminas_faltantes)} de {LAMINAS_POR_SECCION}:")
            print(f"  {texto_faltantes}")
    print("*" * 45)

def buscar_intercambio(coleccionistas):
    print("\n--- Buscar Intercambio ---")
    if len(coleccionistas) < 2:
        print("Se necesitan al menos 2 coleccionistas.")
        return

    nombre_a = input("Primer coleccionista: ")
    coleccionista_a = buscar_coleccionista(coleccionistas, nombre_a)
    if coleccionista_a is None:
        print(f"Error: no se encontró a '{nombre_a}'.")
        return

    nombre_b = input("Segundo coleccionista: ")
    if nombre_a == nombre_b:
        print("Error: deben ser dos coleccionistas distintos.")
        return

    coleccionista_b = buscar_coleccionista(coleccionistas, nombre_b)
    if coleccionista_b is None:
        print(f"Error: no se encontró a '{nombre_b}'.")
        return

    a_ofrece_b = []
    for codigo in coleccionista_a["laminas_repetidas"]:
        if codigo not in coleccionista_b["laminas_pegadas"]:
            a_ofrece_b.append(codigo)

    b_ofrece_a = []
    for codigo in coleccionista_b["laminas_repetidas"]:
        if codigo not in coleccionista_a["laminas_pegadas"]:
            b_ofrece_a.append(codigo)

    if len(a_ofrece_b) == 0 and len(b_ofrece_a) == 0:
        print(f"\nNo hay intercambios posibles entre '{nombre_a}' y '{nombre_b}'.")
        return

    print(f"\nIntercambios entre {nombre_a} y {nombre_b}:")
    if len(a_ofrece_b) > 0:
        print(f"  {nombre_a} ofrece a {nombre_b}: {', '.join(a_ofrece_b)}")
    else:
        print(f"  {nombre_a} no tiene nada útil para {nombre_b}.")

    if len(b_ofrece_a) > 0:
        print(f"  {nombre_b} ofrece a {nombre_a}: {', '.join(b_ofrece_a)}")
    else:
        print(f"  {nombre_b} no tiene nada útil para {nombre_a}.")

# =============================================================================
# PROGRAMA PRINCIPAL
# =============================================================================
def main():
    coleccionistas = []
    
    while True:
        print("\n========== MENÚ ÁLBUM MUNDIAL ==========")
        print("1. Registrar coleccionista")
        print("2. Pegar lámina")
        print("3. Marcar lámina repetida")
        print("4. Buscar coleccionista")
        print("5. Ver láminas faltantes por sección")
        print("6. Buscar intercambio entre dos coleccionistas")
        print("7. Salir")
        print("==========================================")
        
        try:
            opcion = int(input("Seleccione una opción (1-7): "))
            if not (1 <= opcion <= 7):
                print("Error: ingrese un número entre 1 y 7.")
                continue
        except ValueError:
            print("Error: debe ingresar un número entero válido.")
            continue

        if opcion == 1:
            registrar_coleccionista(coleccionistas)
        elif opcion == 2:
            pegar_lamina(coleccionistas)
        elif opcion == 3:
            marcar_lamina_repetida(coleccionistas)
        elif opcion == 4:
            mostrar_coleccionista(coleccionistas)
        elif opcion == 5:
            ver_laminas_faltantes(coleccionistas)
        elif opcion == 6:
            buscar_intercambio(coleccionistas)
        elif opcion == 7:
            print("\n¡Gracias por coleccionar con nosotros! Hasta la próxima.")
            break

if __name__ == "__main__":
    main()