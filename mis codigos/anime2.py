# ============================================
# PLANTILLA DE PRÁCTICA - AniStream
# Rellena cada función tú mismo. No mires la solución
# hasta que lo hayas intentado sin ayuda.
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
    # 1. Normalizo 'genero' para comparar sin importar mayúsculas/espacios.
    genero_buscado = genero.strip().lower()
    total = 0
    # 2 y 3. Recorro 'series', y cuando el género coincide, sumo los
    #        episodios desde 'catalogo' usando el mismo código.
    for codigo, datos in series.items():
        if datos[IDX_GENERO].lower() == genero_buscado:
            total += catalogo[codigo][IDX_EPISODIOS]
    # 4. Solo imprimo, no retorno nada.
    print(f"Total de episodios del género '{genero}': {total}")


# ---------- OPCIÓN 2: Búsqueda por rango de precio ----------
def busqueda_precio(p_min, p_max):
    resultados = []
    # 1. Recorro 'catalogo' revisando las dos condiciones.
    for codigo, datos in catalogo.items():
        precio = datos[IDX_PRECIO]
        episodios = datos[IDX_EPISODIOS]
        if p_min <= precio <= p_max and episodios > 0:
            # 2. Armo "Titulo--Codigo" usando el título desde 'series'.
            titulo = series[codigo][IDX_TITULO]
            resultados.append(f"{titulo}--{codigo}")

    if resultados:
        # 3. Ordeno alfabéticamente (por defecto sort() ordena por el string completo,
        #    y como empieza con el título, queda ordenado por título).
        resultados.sort()
        for r in resultados:
            print(r)
    else:
        # 4. Lista vacía -> aviso que no hay resultados.
        print("No se encontraron series en ese rango de precio.")


# ---------- OPCIÓN 3: Actualizar precio ----------
def actualizar_precio(codigo, nuevo_precio):
    # 1. Normalizo el código para que la búsqueda sea case-insensitive.
    codigo = codigo.upper()
    # 2 y 3. Si existe, actualizo y retorno True; si no, False.
    #        Sin prints acá: el menú decide qué mostrar.
    if codigo in catalogo:
        catalogo[codigo][IDX_PRECIO] = nuevo_precio
        return True
    return False


# ---------- OPCIÓN 4: Validaciones individuales ----------
# Regla de oro: cada una de estas SOLO retorna True/False. Cero prints.

def validar_titulo(titulo):
    # .strip() elimina espacios; bool("") es False, bool("algo") es True.
    return bool(titulo.strip())

def validar_genero(genero):
    return bool(genero.strip())

def validar_estudio(estudio):
    return bool(estudio.strip())

def validar_clasificacion(clasificacion):
    # Debe ser EXACTAMENTE uno de estos tres valores (mayúsculas incluidas,
    # porque el enunciado no dice que sea case-insensitive acá).
    return clasificacion in ('G', 'PG', 'M')

def validar_subtitulado(valor):
    # .lower() para aceptar 'S' o 's' por igual.
    return valor.lower() in ('s', 'n')

def validar_pais_origen(pais):
    return bool(pais.strip())

def validar_precio(precio):
    # isinstance revisa el tipo; ya viene como int porque se convirtió antes
    # con int(), pero igual lo comprobamos por si acaso.
    return isinstance(precio, int) and precio > 0

def validar_episodios(episodios):
    return isinstance(episodios, int) and episodios >= 0


def agregar_serie(codigo, titulo, genero, estudio, clasificacion,
                   subtitulado, pais_origen, precio, episodios):
    codigo = codigo.upper()
    # No se permiten códigos duplicados.
    if codigo in series:
        return False
    # Agrego a AMBOS diccionarios, respetando el orden de campos exigido.
    series[codigo] = [titulo, genero, estudio, clasificacion, subtitulado, pais_origen]
    catalogo[codigo] = [precio, episodios]
    return True


# ---------- OPCIÓN 5: Eliminar serie ----------
def eliminar_serie(codigo):
    codigo = codigo.upper()
    if codigo in series:
        # Elimino de AMBOS diccionarios para que queden sincronizados.
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
            # Bandera + while: no avanzo hasta tener dos enteros válidos.
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
            while seguir == "s":  # while exterior: repetir mientras diga 's'
                codigo = input("Código de la serie: ")

                precio_valido = False
                while not precio_valido:  # while interior: forzar entero válido
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
                    continue  # vuelve al menú, no sigue validando el resto

                # if/elif en cadena: se muestra SOLO el primer error encontrado.
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
                    # Todo válido: convierto 's'/'n' a booleano recién acá.
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