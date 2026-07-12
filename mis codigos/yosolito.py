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

def contar_episodios_por_genero(genero_a_buscar):
    genero_a_buscar = genero_a_buscar.lower()
    contador_de_episodios = 0
    for codigo,datos_serie in series.items():
        if datos_serie[IDX_GENERO].lower() == genero_a_buscar.lower():
            contador_de_episodios += catalogo[codigo][IDX_EPISODIOS]
    print(f"los episodios para el genero {genero_a_buscar} son de {contador_de_episodios} episodios")

def busqueda_de_serie_por_rango_de_precio(precio_minimo,precio_maximo):
    lista_de_series_encontradas = []
    for codigo,datos_serie in catalogo.items():
        precio_actual = datos_serie[IDX_PRECIO]# hay que poner los datos para saber d edonde sacarlos
        episodios_actuales = datos_serie[IDX_EPISODIOS]

        precio_dentro_del_rango = precio_minimo <= precio_actual <= precio_maximo
        episodios_mayor_a_0 = episodios_actuales > 0

        if precio_dentro_del_rango and episodios_mayor_a_0:
            #agregar los animes encontrados a la lista
            titulo_serie = series[codigo][IDX_TITULO]
            lista_de_series_encontradas.append(f"{titulo_serie}--{codigo}")
    
    if len(lista_de_series_encontradas) ==  0: #si no encuentra nada tiene que retornar 
        print("no se encuntran animes con ese rango de precios")
        return
    lista_de_series_encontradas.sort()# sort es para ordenar la lista albafetecamente 
    for linea in lista_de_series_encontradas:
        print(linea)


def actualizar_precio(codigo,precio_nuevo):
    codigo = codigo.upper()
    if codigo in catalogo: #ponemos codigo in catalogo ya que ahi se encontra los precios
        catalogo[codigo][IDX_PRECIO] = precio_nuevo #es el codigo para saber que anime es y el precio ya qe eso vamos a modificar
        return True
    return False
#primero validamos todo y luego agregamos
def validar_titulo(titulo):
    return titulo.strip() != ""
def validar_genero(genero):
    return genero.strip() != ""
def validar_estudio(estudio):
    return estudio.strip() != ""
def validar_clasificacion(clasificacion):
    return clasificacion.upper() in ("G","PG","M")
def validar_subtitulos(subtitulos):
    return subtitulos.lower() in ("s","n")
def validar_pais(pais):
    return pais.strip() != ""
def validar_precio(precio):
    return isinstance(precio, int) and precio > 0
def validar_capitulos(episodios):
    return isinstance(episodios, int) and episodios > 0

def agregar_serie(codigo,titulo,genero,estudio,clasificacion,subtitulos,pais,precio,episodios):
    codigo = codigo.upper()
    if codigo in series:# si el codigo ya existe retornamos false
        return False
    series[codigo] = [titulo,genero,estudio,clasificacion,subtitulos,pais]# si el codigo no existe pasamos a agregar la serie y catalogo y retornamos true 
    catalogo[codigo] = [precio,episodios]
    return True

def eliminar_serie(codigo):
    codigo = codigo.upper()
    if codigo in series:
        del series[codigo] #del elimina todo la info del anime mediante el codigo
        del catalogo[codigo]
        return True
    return False

def mostrar_menu():
    print("===========================================")
    print("                  MENU                            ")
    print("1. episodios por genero")
    print("2. busqueda de series por rango de precios")
    print("3. actualizar precio de serie")
    print("4. agregar serie")
    print("5. eliminar serie")
    print("6. salir del programa")
    print("============================================")

def ejecutar_programa():
    codigo_funcionando = True
    while codigo_funcionando:
        mostrar_menu()
        opcion_seleccionada = input("que opcion quieres escojer? ")
        if opcion_seleccionada == "1":
            genero_a_buscar = input("que genero buscas?")
            contar_episodios_por_genero(genero_a_buscar)

        elif opcion_seleccionada == "2":
            datos_ingresados_corractamente = False #ponemos una vandera false para que cuando los digitos esten bien sea verdad y se rompa el while
            while not datos_ingresados_corractamente:
                try:
                    precio_minimo = int(input("cual es tu precio minimo? "))
                    precio_maximo = int(input("cual es tu precio maximo? "))
                    busqueda_de_serie_por_rango_de_precio(precio_minimo,precio_maximo)
                    datos_ingresados_corractamente = True
                except ValueError:
                    print("tiene que ser un numero mayor a 0 y entero")
        elif opcion_seleccionada == "3":
            seguir_actualizando = True
            while seguir_actualizando:
                codigo = input("danos el codigo de la serie que quieres modificar el precio")
                try:
                    precio_nuevo = int(input("cual es el nuevo precio? "))
                    actualizacion_exitosa = actualizar_precio(codigo,precio_nuevo)
                    if actualizacion_exitosa:
                        print("actualizacion con exito")
                    else:
                        print("error al intentar actualizar el codigo,intente nuevamente")
                except ValueError:
                    print("tiene que ser un numero positivo y entero")

                respuesta_a_subtitulos = input("tiene subtitulos? (s/n)")
                if respuesta_a_subtitulos.lower() != "s":
                    seguir_actualizando = False #si la respuesta es diferente a n se rompre el while

        elif opcion_seleccionada == "4":
            print("ahora danos los datos de la serie a agregar") #agregamos 
            codigo_agregar = input("cual es su codigo? ")
            titulo_agregar = input("cual es su titulo? ")
            genero_agregar = input("cual es su genero? ")
            estudio_agregar = input("cual es su estudio? ")
            clasificacion_agregar = input("cual es su clasificacion? ")
            subtitulos_agregar = input("tiene subtitulos? ")
            pais_agregar = input("de que pais es? ")

            datos_validos = True
            #ahora validamos 
            if not validar_titulo(titulo_agregar):
                datos_validos = False
            if not validar_genero(genero_agregar):
                datos_validos = False
            if not validar_estudio(estudio_agregar):
                datos_validos = False
            if not validar_clasificacion(clasificacion_agregar):
                print("tiene que ser (G,PG O M)")
                datos_validos = False
            if not validar_subtitulos(subtitulos_agregar):
                print("tiene que ser s o n")
                datos_validos = False
            if not validar_pais(pais_agregar):
                datos_validos = False
            try:
                precio_agregar = int(input("cual es su precio? "))
                episodios_agregar = int(input("cuantos episodios tiene? "))
                if not validar_precio(precio_agregar):
                    datos_validos = False
                if not validar_capitulos(episodios_agregar):
                    datos_validos = False
            except ValueError:
                print("tiene que ser un numero positivo entero")
                datos_validos = False

            if datos_validos:
                subititulos = subtitulos_agregar.lower() == "s"
                agregado_exitosamente = agregar_serie(codigo_agregar,titulo_agregar,genero_agregar,estudio_agregar,clasificacion_agregar,subititulos,pais_agregar,precio_agregar,episodios_agregar)   
                if agregado_exitosamente:
                    print("serie agregada")
                else:
                    print("erro al agregar la serie") 
        elif opcion_seleccionada == "5":
            codigo = input("cual es el codigo de la serie? ") 
            eliminacion_exitosa = eliminar_serie(codigo)
            if eliminacion_exitosa :
                print("anime eliminado")
            else:
                print("error al eliminar el codigo")
            
           
                
                    


        





        elif  opcion_seleccionada == "6":
            print("hasta pronto....")
            codigo_funcionando = False








ejecutar_programa()













