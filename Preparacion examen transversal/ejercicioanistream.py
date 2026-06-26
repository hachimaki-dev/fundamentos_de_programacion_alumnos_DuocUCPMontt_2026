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

def mostrarMenu():
    print("""
========== MENÚ PRINCIPAL ==========
1. Episodios por género
2. Búsqueda de series por rango de precio
3. Actualizar precio de serie
4. Agregar serie
5. Eliminar serie
6. Salir
=====================================""")
def episodios(genero):
    genero= genero.casefold()
    episodios=0
    for i in series.items():
        #print(i)
        for n in i[1]:
            if n == genero:
                anime=i[0]
                episodios+=catalogo[anime][1]
    print(f"{episodios} episodios")            

#episodios("accion")
def opcionMenu():
    while True:
        opcion= input("Por favor elige una opción: ")
        if opcion in ['1','2','3','4','5','6']:
            return opcion
        print('Ingrese una opcion valida.')
def main():
    while True:
        mostrarMenu()
        seleccion=opcionMenu()
        if seleccion == '1':
            generoBuscar=input('¿Que género desea buscar?: ')
            episodios(generoBuscar)
        if seleccion == '6':
            break    


main()    