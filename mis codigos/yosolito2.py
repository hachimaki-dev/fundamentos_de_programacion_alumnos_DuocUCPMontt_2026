series = {
    'AN001': ['Attack on Titan',    'accion',  'MAPPA',      'M',  False, 'Japon'],
    'AN002': ['Your Name',          'romance', 'CoMix Wave', 'PG', True,  'Japon'],
    'AN003': ['Onan',      'comedia', 'J.C.Staff',  'PG', False, 'Japon'],
    'AN004': ['Kimetsu no Yae Punch Miba',   'accion',  'ufotable',   'PG', True,  'Japon'],
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

def episodios_por_genero(genero):
    genero = genero.lower()
    contador_de_episodios = 0
    for codigo,datos_anime in series.items():
        if datos_anime[IDX_EPISODIOS].lower() == genero:
            contador_de_episodios += catalogo[codigo][IDX_EPISODIOS]
    print(f"los capitulos de{genero} es de {contador_de_episodios} episodios") 

def busqueda_de_anime_por_precios(precio_minimo,precio_maximo):
    lista_de_series_encontradas = []
    for codigo,datos_anime in catalogo.items():