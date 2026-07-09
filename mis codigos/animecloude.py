# ============================================
#  ANISTREAM - Sistema de administracion de catalogo
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

# ---- indices serie ----
IDX_TITULO = 0
IDX_GENERO = 1
IDX_ESTUDIO = 2
IDX_CLASIFICACION = 3
IDX_SUBTITULADO = 4
IDX_PAIS = 5

# ---- indices catalogo ----
IDX_PRECIO = 0
IDX_EPISODIOS = 1


# =========================================================
# OPCION 1: Episodios por genero
# =========================================================
def contar_episodios_por_genero(genero_a_buscar):
    genero_a_buscar = genero_a_buscar.lower()
    total_de_episodios_por_genero = 0

    for codigo_serie, datos_serie in series.items():
        if datos_serie[IDX_GENERO].lower() == genero_a_buscar:
            total_de_episodios_por_genero += catalogo[codigo_serie][IDX_EPISODIOS]

    print(f"Total de episodios disponibles para el genero '{genero_a_buscar}': {total_de_episodios_por_genero}")


# =========================================================
# OPCION 2: Busqueda de series por rango de precio
# =========================================================
def buscar_series_por_rango_de_precio(precio_minimo, precio_maximo):
    lista_series_encontradas = []

    for codigo_serie, datos_catalogo in catalogo.items():
        precio_actual = datos_catalogo[IDX_PRECIO]
        episodios_actuales = datos_catalogo[IDX_EPISODIOS]

        precio_dentro_del_rango = precio_minimo <= precio_actual <= precio_maximo
        tiene_episodios_disponibles = episodios_actuales > 0

        if precio_dentro_del_rango and tiene_episodios_disponibles:
            titulo_serie = series[codigo_serie][IDX_TITULO]
            lista_series_encontradas.append(f"{titulo_serie}--{codigo_serie}")

    if len(lista_series_encontradas) == 0:
        print("No se encontraron series dentro de ese rango de precio.")
        return

    lista_series_encontradas.sort()
    for linea_resultado in lista_series_encontradas:
        print(linea_resultado)


# =========================================================
# OPCION 3: Actualizar precio de una serie
# =========================================================
def actualizar_precio_de_serie(codigo, nuevo_precio):
    codigo = codigo.upper()
    if codigo in catalogo:
        catalogo[codigo][IDX_PRECIO] = nuevo_precio
        return True
    return False


# =========================================================
# OPCION 4: Agregar serie -> funciones de validacion, una por campo
# =========================================================
def validar_texto_no_vacio(texto):
    return texto.strip() != ""

def validar_clasificacion(clasificacion):
    return clasificacion.upper() in ('G', 'PG', 'M')

def validar_respuesta_subtitulado(respuesta):
    return respuesta.lower() in ('s', 'n')

def validar_precio(precio):
    return isinstance(precio, int) and precio > 0

def validar_episodios(episodios):
    return isinstance(episodios, int) and episodios >= 0

def agregar_serie(codigo, titulo, genero, estudio, clasificacion, subtitulado, pais_origen, precio, episodios):
    codigo = codigo.upper()
    if codigo in series:
        return False
    series[codigo] = [titulo, genero, estudio, clasificacion, subtitulado, pais_origen]
    catalogo[codigo] = [precio, episodios]
    return True


# =========================================================
# OPCION 5: Eliminar serie
# =========================================================
def eliminar_serie(codigo):
    codigo = codigo.upper()
    if codigo in series:
        del series[codigo]
        del catalogo[codigo]
        return True
    return False


# =========================================================
# OPCION 7: Ver series agregadas
# =========================================================
def mostrar_todas_las_series():
    if len(series) == 0:
        print("No hay series registradas.")
        return

    for codigo_serie, datos_serie in series.items():
        titulo = datos_serie[IDX_TITULO]
        genero = datos_serie[IDX_GENERO]
        editorial = datos_serie[IDX_ESTUDIO]
        clasifiacion = datos_serie[IDX_CLASIFICACION]
        precio_actual = catalogo[codigo_serie][IDX_PRECIO]
        episodios_actuales = catalogo[codigo_serie][IDX_EPISODIOS]
        print(f"{codigo_serie} | {titulo} | {genero} |{editorial} |{clasifiacion}|${precio_actual} | {episodios_actuales} episodios")


# =========================================================
# MENU PRINCIPAL
# =========================================================
def mostrar_menu():
    print("\n========== MENU PRINCIPAL ==========")
    print("1. Episodios por genero")
    print("2. Busqueda de series por rango de precio")
    print("3. Actualizar precio de serie")
    print("4. Agregar serie")
    print("5. Eliminar serie")
    print("6. Ver series agregadas")
    print("7. Salir")
    print("=====================================")


def ejecutar_programa():
    programa_activo = True

    while programa_activo:
        mostrar_menu()
        opcion_elegida = input("Seleccione una opcion: ")

        if opcion_elegida == "1":
            genero_pedido = input("Ingrese el genero a buscar: ")
            contar_episodios_por_genero(genero_pedido)

        elif opcion_elegida == "2":
            datos_ingresados_correctamente = False
            while not datos_ingresados_correctamente:
                try:
                    precio_min = int(input("Ingrese el precio minimo: "))
                    precio_max = int(input("Ingrese el precio maximo: "))
                    datos_ingresados_correctamente = True
                except ValueError:
                    print("Debe ingresar numeros enteros validos, intente de nuevo.")

            buscar_series_por_rango_de_precio(precio_min, precio_max)

        elif opcion_elegida == "3":
            seguir_actualizando = True
            while seguir_actualizando:
                codigo_ingresado = input("Ingrese el codigo de la serie: ")
                try:
                    precio_nuevo = int(input("Ingrese el nuevo precio: "))
                    actualizacion_exitosa = actualizar_precio_de_serie(codigo_ingresado, precio_nuevo)
                    if actualizacion_exitosa:
                        print("Precio actualizado correctamente.")
                    else:
                        print("El codigo ingresado no existe.")
                except ValueError:
                    print("El precio debe ser un numero entero.")

                respuesta = input("¿Desea actualizar otro precio (s/n)? ")
                if respuesta.lower() != "s":
                    seguir_actualizando = False

        elif opcion_elegida == "4":
            codigo_nuevo = input("Codigo: ")
            titulo_nuevo = input("Titulo: ")
            genero_nuevo = input("Genero: ")
            estudio_nuevo = input("Estudio: ")
            clasificacion_nueva = input("Clasificacion (G/PG/M): ")
            respuesta_subtitulado = input("¿Subtitulada? (s/n): ")
            pais_nuevo = input("Pais de origen: ")

            datos_validos = True

            if not validar_texto_no_vacio(titulo_nuevo):
                print("El titulo no puede estar vacio.")
                datos_validos = False
            if not validar_texto_no_vacio(genero_nuevo):
                print("El genero no puede estar vacio.")
                datos_validos = False
            if not validar_texto_no_vacio(estudio_nuevo):
                print("El estudio no puede estar vacio.")
                datos_validos = False
            if not validar_clasificacion(clasificacion_nueva):
                print("La clasificacion debe ser G, PG o M.")
                datos_validos = False
            if not validar_respuesta_subtitulado(respuesta_subtitulado):
                print("Debe responder s o n.")
                datos_validos = False
            if not validar_texto_no_vacio(pais_nuevo):
                print("El pais no puede estar vacio.")
                datos_validos = False

            try:
                precio_nuevo = int(input("Precio: "))
                episodios_nuevos = int(input("Episodios: "))
                if not validar_precio(precio_nuevo):
                    print("El precio debe ser un entero mayor que cero.")
                    datos_validos = False
                if not validar_episodios(episodios_nuevos):
                    print("Los episodios deben ser un entero mayor o igual a cero.")
                    datos_validos = False
            except ValueError:
                print("Precio y episodios deben ser numeros enteros.")
                datos_validos = False

            if datos_validos:
                subtitulado_booleano = respuesta_subtitulado.lower() == "s"
                agregado_exitoso = agregar_serie(
                    codigo_nuevo, titulo_nuevo, genero_nuevo, estudio_nuevo,
                    clasificacion_nueva, subtitulado_booleano, pais_nuevo,
                    precio_nuevo, episodios_nuevos
                )
                if agregado_exitoso:
                    print("Serie agregada correctamente.")
                else:
                    print("Ese codigo ya existe.")

        elif opcion_elegida == "5":
            codigo_a_eliminar = input("Ingrese el codigo de la serie a eliminar: ")
            eliminacion_exitosa = eliminar_serie(codigo_a_eliminar)
            if eliminacion_exitosa:
                print("Serie eliminada correctamente.")
            else:
                print("El codigo ingresado no existe.")

        elif opcion_elegida == "6":
            mostrar_todas_las_series()

        elif opcion_elegida == "7":
            print("Gracias por usar AniStream. Hasta luego!")
            programa_activo = False

        else:
            print("Debe seleccionar una opcion valida")


ejecutar_programa()