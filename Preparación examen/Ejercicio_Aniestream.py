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

menu = ['1', '2', '3', '4', '5', '6']

def mostrarmenu():
    print("""========== MENÚ PRINCIPAL ==========
1. Episodios por género
2. Búsqueda de series por rango de precio
3. Actualizar precio de serie
4. Agregar serie
5. Eliminar serie
6. Salir
=====================================""")

def elegirOpcion():
    while True:
        opcion = input("Ingresa una opción: ")
        if opcion in menu:
            return opcion
        else:
            print("Ingresa una opción válida")

def episodiosGenero(genero):
    acumulador = 0

    for cada_serie in series.items():
        codigo_anime = cada_serie[0]
        if cada_serie[1][1] == genero:
            for cada_item in catalogo.items():
                if cada_item[0] == codigo_anime:
                    acumulador += cada_item[1][1]
    return acumulador


def main():
    while True:
        mostrarmenu()
        opcion_elegida = elegirOpcion()

        if opcion_elegida == '6':
            break

        elif opcion_elegida == '1':
            episodios = episodiosGenero('accion')
            print(episodios)
        
        elif opcion_elegida == '2':
            pass
        elif opcion_elegida == '3':
            pass
        elif opcion_elegida == '4':
            pass
        elif opcion_elegida == '5':
            pass
      
main()