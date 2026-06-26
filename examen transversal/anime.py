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
def mostrarmenu():
    print("""========== MENÚ PRINCIPAL ==========
1. Episodios por género
2. Búsqueda de series por rango de precio
3. Actualizar precio de serie
4. Agregar serie
5. Eliminar serie
6. Salir
=====================================""")
def episodios_genero(genero):
    acumaldor_de_cantidad = 0
    for i in series.items():
        codigo_anime = i[0]
        if i[1][1] == genero:
            for cada_item_catalogo in catalogo.items():
                if cada_item_catalogo[0] == codigo_anime:
                    acumaldor_de_cantidad += cada_item_catalogo[1][1]
    return acumaldor_de_cantidad
resultado_cantidad = episodios_genero("drama")
print(resultado_cantidad)
                    
        