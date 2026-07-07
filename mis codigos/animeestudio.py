# ============================================
# Sistema de gestión AniStream
# ============================================

series = {
    'AN001': ['Attack on Titan',    'accion',  'MAPPA',      'M',  False, 'Japon'],
    'AN002': ['Your Name',          'romance', 'CoMix Wave', 'PG', True,  'Japon'],
    'AN003': ['One Punch Man',      'comedia', 'J.C.Staff',  'PG', False, 'Japon'],
    'AN004': ['Kimetsu no Yaiba',   'accion',  'ufotable',   'PG', True,  'Japon'],
    'AN005': ['No Game No Life',    'isekai',  'Madhouse',   'PG', True,  'Japon'],
    'AN006': ['Violet Evergarden',  'drama',   'KyoAni',     'G',  True,  'Japon'],
}

catalogo = {
    'AN001': [9990,  75],
    'AN002': [4990,   0],
    'AN003': [7990,  12],
    'AN004': [8990,  26],
    'AN005': [5990,  13],
    'AN006': [6990,  13],
}

# Constantes para las posiciones de cada lista.
# Esto es solo para que el código sea más legible: series[codigo][IDX_GENERO]
# se entiende mejor que series[codigo][1]. En la prueba puedes usar
# directamente los números si te da más seguridad, es lo mismo.
IDX_TITULO = 0
IDX_GENERO = 1
IDX_ESTUDIO = 2
IDX_CLASIFICACION = 3
IDX_SUBTITULADO = 4
IDX_PAIS = 5

IDX_PRECIO = 0
IDX_EPISODIOS = 1


# ---------- OPCIÓN 1: Episodios por género ----------
def episodios_genero(genero):
    total = 0
    genero_buscado = genero.strip().lower()
    for codigo, datos in series.items():
        if datos[IDX_GENERO].lower() == genero_buscado:
            total += catalogo[codigo][IDX_EPISODIOS]
    print(f"Total de episodios del género '{genero}': {total}")


# ---------- OPCIÓN 2: Búsqueda por rango de precio ----------
def busqueda_precio(p_min, p_max):
    resultados = []
    for codigo, datos in catalogo.items():
        precio = datos[IDX_PRECIO]
        episodios = datos[IDX_EPISODIOS]
        if p_min <= precio <= p_max and episodios > 0:
            titulo = series[codigo][IDX_TITULO]
            resultados.append(f"{titulo}--{codigo}")

    if resultados:
        resultados.sort()
        for r in resultados:
            print(r)
    else:
        print("No se encontraron series en ese rango de precio.")


# ---------- OPCIÓN 3: Actualizar precio ----------
def actualizar_precio(codigo, nuevo_precio):
    codigo = codigo.upper()
    if codigo in catalogo:
        catalogo[codigo][IDX_PRECIO] = nuevo_precio
        return True
    return False


# ---------- OPCIÓN 4: Agregar serie (validaciones individuales) ----------
def validar_titulo(titulo):
    return bool(titulo.strip())

def validar_genero(genero):
    return bool(genero.strip())

def validar_estudio(estudio):
    return bool(estudio.strip())

def validar_clasificacion(clasificacion):
    return clasificacion in ('G', 'PG', 'M')

def validar_subtitulado(valor):
    return valor.lower() in ('s', 'n')

def validar_pais_origen(pais):
    return bool(pais.strip())

def validar_precio(precio):
    return isinstance(precio, int) and precio > 0

def validar_episodios(episodios):
    return isinstance(episodios, int) and episodios >= 0


def agregar_serie(codigo, titulo, genero, estudio, clasificacion,
                   subtitulado, pais_origen, precio, episodios):
    codigo = codigo.upper()
    if codigo in series:
        return False
    series[codigo] = [titulo, genero, estudio, clasificacion, subtitulado, pais_origen]
    catalogo[codigo] = [precio, episodios]
    return True


# ---------- OPCIÓN 5: Eliminar serie ----------
def eliminar_serie(codigo):
    codigo = codigo.upper()
    if codigo in series:
        del series[codigo]
        del catalogo[codigo]
        return True
    return False


# ============================================
# PROGRAMA PRINCIPAL (menú)
# ============================================
def menu():
    while True:
        print("\n========== MENÚ PRINCIPAL ==========")
        print("1. Episodios por género")
        print("2. Búsqueda de series por rango de precio")
        print("3. Actualizar precio de serie")
        print("4. Agregar serie")
        print("5. Eliminar serie")
        print("6. Salir")
        print("=====================================")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            genero = input("Ingrese el género a buscar: ")
            episodios_genero(genero)

        elif opcion == "2":
            datos_validos = False
            while not datos_validos:
                try:
                    p_min = int(input("Precio mínimo: "))
                    p_max = int(input("Precio máximo: "))
                    datos_validos = True
                except ValueError:
                    print("Debe ingresar números enteros válidos. Intente nuevamente.")
            busqueda_precio(p_min, p_max)

        elif opcion == "3":
            seguir = "s"
            while seguir == "s":
                codigo = input("Código de la serie: ")

                precio_valido = False
                while not precio_valido:
                    try:
                        nuevo_precio = int(input("Nuevo precio: "))
                        precio_valido = True
                    except ValueError:
                        print("El precio debe ser un número entero. Intente nuevamente.")

                if actualizar_precio(codigo, nuevo_precio):
                    print("Precio actualizado con éxito.")
                else:
                    print("Código no encontrado.")

                seguir = input("¿Desea actualizar otro precio (s/n)? ").lower()

        elif opcion == "4":
            codigo = input("Código: ").upper()
            if codigo in series:
                print("Ese código ya existe.")
            else:
                titulo = input("Título: ")
                genero = input("Género: ")
                estudio = input("Estudio: ")
                clasificacion = input("Clasificación (G/PG/M): ")
                subtitulado_str = input("¿Subtitulada? (s/n): ")
                pais_origen = input("País de origen: ")

                try:
                    precio = int(input("Precio mensual: "))
                    episodios = int(input("Cantidad de episodios: "))
                except ValueError:
                    print("Precio y episodios deben ser números enteros.")
                    continue

                if not validar_titulo(titulo):
                    print("Título inválido.")
                elif not validar_genero(genero):
                    print("Género inválido.")
                elif not validar_estudio(estudio):
                    print("Estudio inválido.")
                elif not validar_clasificacion(clasificacion):
                    print("Clasificación inválida. Debe ser G, PG o M.")
                elif not validar_subtitulado(subtitulado_str):
                    print("Debe responder 's' o 'n'.")
                elif not validar_pais_origen(pais_origen):
                    print("País de origen inválido.")
                elif not validar_precio(precio):
                    print("El precio debe ser un entero mayor que 0.")
                elif not validar_episodios(episodios):
                    print("Los episodios deben ser un entero mayor o igual a 0.")
                else:
                    subtitulado = subtitulado_str.lower() == 's'
                    if agregar_serie(codigo, titulo, genero, estudio, clasificacion,
                                      subtitulado, pais_origen, precio, episodios):
                        print("Serie agregada con éxito.")
                    else:
                        print("No se pudo agregar la serie.")

        elif opcion == "5":
            codigo = input("Código de la serie a eliminar: ")
            if eliminar_serie(codigo):
                print("Serie eliminada con éxito.")
            else:
                print("Código no encontrado.")

        elif opcion == "6":
            print("Saliendo del sistema...")
            break

        else:
            print("Debe seleccionar una opción válida")


if __name__ == "__main__":
    menu()