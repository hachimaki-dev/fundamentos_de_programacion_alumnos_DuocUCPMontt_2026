series = {
    #codigo     titulo              genero    estudio       clasif sub      pais
    'AN001': ['Attack on Titan',    'accion',  'MAPPA',      'M',  False, 'Japon'],
    'AN002': ['Your Name',          'romance', 'CoMix Wave', 'PG', True,  'Japon'],
    'AN003': ['One Punch Man',      'comedia', 'J.C.Staff',  'PG', False, 'Japon'],
    'AN004': ['Kimetsu no Yaiba',   'accion',  'ufotable',   'PG', True,  'Japon'],
    'AN005': ['No Game No Life',    'isekai',  'Madhouse',   'PG', True,  'Japon'],
    'AN006': ['Violet Evergarden',  'drama',   'KyoAni',     'G',  True,  'Japon'],
}
    #codigo  precio episodios
catalogo = {
    'AN001': [9990,  75],
    'AN002': [4990,   0],
    'AN003': [7990,  12],
    'AN004': [8990,  26],
    'AN005': [5990,  13],
    'AN006': [6990,  13],
}


def validar_codigo(codigo):
    return bool(codigo.strip().upper())

def validar_titulo(titulo):
    return bool(titulo.strip())

def validar_genero(genero):
    return bool(genero.strip().lower())

def validar_autor(estudio):
    return bool(estudio.strip().upper())

def validar_clasificacion(clasificacion):
    return clasificacion.strip().upper() in ["G", "PG", "M"]

def validar_subtitulos(subtitulos_texto):
    return subtitulos_texto.strip().lower() in ["s", "n"]

def validar_pais_origen(pais_origen):
    return bool(pais_origen.strip())

def validar_precio(precio_texto):
    try:
        return int(precio_texto) > 0
    except ValueError:
        return False

def validar_episidios_valor(episodios_texto):
    try:
        return int(episodios_texto) > 0
    except ValueError:
        return False


def episodio_genero(genero):
    int(total_episodio_genero) = 0

    if validar_genero(genero):

        genero_buscado = validar_genero(genero)

        for codigo in series:
            genero_actual = series[codigo][1].strip().lower()

            if genero_actual == genero_buscado:
                cantidad_episodio_genero = int(catalogo[codigo][1])
                total_episodio_genero += cantidad_episodio_genero

        return total_episodio_genero > 0

def validar_busqueda_rango_precio(precio_minimo, precio_maximo):
    resultados_encontrados = []

    for codigo_actual in catalogo:
        precio_actual = catalogo[codigo_actual][0]
        episodios_actual = catalogo[codigo_actual][1]

        if precio_minimo <= precio_actual <= precio_maximo and episodios_actual > 0:
            titulo_actual = series[codigo_actual][0]
            resultados_encontrados.append(f"{codigo_actual} -- {titulo_actual}")
    
    if resultados_encontrados:
        resultados_encontrados.sort()
        print(f"Resultados de la busqueda de rango de precio: {resultados_encontrados}")
    else:
        print(f"No se encontraron series que cumplas con los criterios.")

def actulizar_precio(codigo, precio_nuevo):
    codigo_mayusculas = codigo.append().upper()

    if codigo_mayusculas in catalogo:
        catalogo[codigo_mayusculas][0] == precio_nuevo
        return True
    return False

def agregar_serie(codigo, titulo, genero, estudio, clasificacion, subtitutlos, pais, precio, episodios):
    
    if codigo in series[codigo] or codigo in catalogo[codigo]:
        return False
    
    series[codigo] = [titulo, genero, estudio, clasificacion, subtitutlos, pais]
    catalogo[codigo] = [precio, episodios]

    return True

def eliminar_serie(codigo):
    codigo_mayusculas = codigo.strip().upper()
    if codigo_mayusculas in series[codigo_mayusculas] or codigo_mayusculas in catalogo[codigo_mayusculas]:
        del series[codigo_mayusculas]
        del catalogo[codigo_mayusculas]
        return True
    return False




