series = {
  'AN001': ['Attack on Titan',  'accion', 'MAPPA',   'M', False, 'Japon'],
  'AN002': ['Your Name',     'romance', 'CoMix Wave', 'PG', True, 'Japon'],
  'AN003': ['One Punch Man',   'comedia', 'J.C.Staff', 'PG', False, 'Japon'],
  'AN004': ['Kimetsu no Yaiba', 'accion', 'ufotable', 'PG', True, 'Japon'],
  'AN005': ['No Game No Life',  'isekai', 'Madhouse', 'PG', True, 'Japon'],
  'AN006': ['Violet Evergarden', 'drama', 'KyoAni',  'G', True, 'Japon'],
  'AN007': ['Spirited Away',   'fantasia', 'Ghibli',  'G', True, 'Japon'],
  'AN008': ['Fullmetal Alchemist','accion', 'Bones',   'PG', False, 'Japon'],
  'AN009': ['Death Note',    'suspenso', 'Madhouse', 'M', False, 'Japon'],
  'AN010': ['Jujutsu Kaisen',  'accion', 'MAPPA',   'M', True, 'Japon'],
  'AN011': ['Kaguya-sama',    'comedia', 'A-1 Pictures', 'PG', True, 'Japon'],
  'AN012': ['Chainsaw Man',   'accion', 'MAPPA',   'M', False, 'Japon'],
  'AN013': ['Sousou no Frieren', 'fantasia', 'Madhouse', 'PG', False, 'Japon']
}



catalogo = {
  'AN001': [9990, 75],
  'AN002': [4990, 0],
  'AN003': [7990, 12],
  'AN004': [8990, 26],
  'AN005': [5990, 13],
  'AN006': [6990, 13],
  'AN007': [4500, 5], # Spirited Away
  'AN008': [9500, 64], # Fullmetal Alchemist
  'AN009': [8500, 37], # Death Note
  'AN010': [8990, 24], # Jujutsu Kaisen
  'AN011': [7500, 36], # Kaguya-sama
  'AN012': [8990, 12], # Chainsaw Man
  'AN013': [9990, 28] # Sousou no Frieren
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
def busquedaPrecios(min,max):
    listaresultado=[]
    listanombre=[]
    for i in catalogo.items():
        #print (i[1][0])
        if i[1][0] >= min and i[1][0] <= max:
            listaresultado.append(i[0])
        #print (listaresultado)    
    for i in listaresultado:
        nombre= series[i][0] + "--" + i
        listanombre.append(nombre)
    listanombre.sort()
    print("---")    
    for i in listanombre:    
        print (i)    
#busquedaPrecios(5000,10000)
def actualizarPrecios(code,precio):
    if code in catalogo:
        valor=catalogo.get(code)
        valor.pop(0)
        valor.insert(0,precio)
        catalogo.update({code: valor})
       
    print (catalogo)    
#actualizarPrecios('AN004',1000)
def validacionCodigo():
    print(wip)

def main():
    while True:
        mostrarMenu()
        seleccion=opcionMenu()
        if seleccion == '1':
            generoBuscar=input('¿Que género desea buscar?: ')
            episodios(generoBuscar)
        if seleccion == '2':
            while True:
                try:
                    minimo=int(input("Ingrese el precio minimo: "))
                    while True:
                        maximo=int(input("Ingrese el precio maximo: "))
                        if maximo > minimo:
                            break
                        print ('Ingrese un valor mayor al precio minimo')
                    break    
                except ValueError:
                    print('Ingrese un dato valido')
            busquedaPrecios(minimo,maximo)    
        if seleccion == '3':
            codigo=input('Ingrese el codigo del anime:').upper()
            if codigo not in catalogo:
                print('Codigo del anime no encontrado') 
            if codigo in catalogo:
                while True:
                    try:
                        precionuevo=int(input('Ingrese el nuevo precio: '))
                        break
                    except ValueError:
                        print('Ingrese un dato valido')
                actualizarPrecios(codigo,precionuevo)        

        if seleccion == '6':
            break    


main()    