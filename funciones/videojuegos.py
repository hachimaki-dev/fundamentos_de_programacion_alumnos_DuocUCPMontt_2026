lista_filtrada_precios = []

juegos = {
    'VG001': ['The Legend of Zelda: BOTW', 'aventura',  'Nintendo',        'E10+', True,  'Japon'],
    'VG002': ['God of War Ragnarok',       'accion',    'Santa Monica',    'M',    True,  'EEUU'],
    'VG003': ['Stardew Valley',            'simulacion','ConcernedApe',    'E',    True,  'EEUU'],
    'VG004': ['Elden Ring',                'rpg',       'FromSoftware',    'M',    True,  'Japon'],
    'VG005': ['Among Us',                  'fiesta',    'Innersloth',      'E10+', False, 'EEUU'],
    'VG006': ['Hades',                     'accion',    'Supergiant Games','T',    True,  'EEUU'],
    'VG007': ['Minecraft',                 'sandbox',   'Mojang',          'E10+', True,  'Suecia'],
    'VG008': ['Persona 5',                 'rpg',       'Atlus',           'M',    False, 'Japon'],
    'VG009': ['Portal 2',                  'puzzle',    'Valve',           'E10+', False, 'EEUU'],
    'VG010': ['Celeste',                   'plataforma','Maddy Makes Games','E10+',True,  'Canada'],
    'VG011': ['Overwatch 2',               'accion',    'Blizzard',        'T',    True,  'EEUU'],
    'VG012': ['Baldur\'s Gate 3',          'rpg',       'Larian Studios',  'M',    True,  'Belgica'],
    'VG013': ['Animal Crossing: NH',       'simulacion','Nintendo',        'E',    False, 'Japon'],
}
 
catalogo_juegos = {
    'VG001': [39990, 120],  # precio, horas de juego estimadas
    'VG002': [59990, 35],
    'VG003': [9990, 60],
    'VG004': [49990, 80],
    'VG005': [4990, 0],
    'VG006': [19990, 25],
    'VG007': [24990, 500],
    'VG008': [34990, 90],
    'VG009': [14990, 10],
    'VG010': [12990, 8],
    'VG011': [0, 40],      # free to play
    'VG012': [54990, 150],
    'VG013': [44990, 200],
}


def cantidad_juegos_en_rango_de_precio(precio_maximo, precio_minimo):
    for cada_catalogo in catalogo_juegos.items():
        if cada_catalogo[1][0] >= precio_minimo and cada_catalogo[1][0] <= precio_maximo and cada_catalogo:
            if cada_catalogo[1][0] >= precio_minimo and cada_catalogo[1][0] <= precio_maximo and cada_catalogo[1][1]:
            for cada_juego in juegos.items():
                if cada_catalogo[0] == cada_juego[1]:
                    datos = cada_juego[1][0] + "--" + cada_juego[0]
                    lista_filtrada_precios.append(datos)
                    
                    lista_filtrada_precios.sort
    return lista_filtrada_precios

def contar_juegos_genero(el_genero):
    acumulador_cantidad_juegos = 0
    for cada_juego in juegos.items():
        if cada_juego[1][1] == el_genero:
            for cada_juego_catalogo in juegos.items():
                if cada_juego_catalogo[0] == cada_juego[0]:
                    acumulador_cantidad_juegos += cada_juego_catalogo[1][1]
    return acumulador_cantidad_juegos

respuesta = cantidad_juegos_en_rango_de_precio(4000,50000)

print(respuesta)
    