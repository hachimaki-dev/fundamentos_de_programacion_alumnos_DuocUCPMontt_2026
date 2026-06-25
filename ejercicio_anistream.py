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
def episodios_por_genero(género):
    
    if género in ['accion', 'romance','comedia','isekai','drama']:
        for código_anime in series.values():
            if código_anime[1] == género:
                print(código_anime[1])
                código_anime_value = código_anime[1]
                for código_ánime_catalogo in catalogo.items():
                    print(código_ánime_catalogo[0])
                  
                    if código_anime_value == código_ánime_catalogo[0]:
                        print(código_ánime_catalogo[1][1])

            else: continue
        print(f"Cápitulos")
    else:
        print("No enccontrado")
genero_a_buscar = input("Ingrese el género: ")
episodios_por_genero(genero_a_buscar)
