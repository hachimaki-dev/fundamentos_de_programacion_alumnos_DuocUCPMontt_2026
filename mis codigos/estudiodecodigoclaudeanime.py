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
    total_de_episodios_por_genero = 0
    for codigo_serie, datos_de_anime in series.items():
        if datos_de_anime[IDX_GENERO].lower() == genero_a_buscar:
            total_de_episodios_por_genero += catalogo[IDX_EPISODIOS[codigo_serie]]
    print(f"los capitulos que hay para{genero_a_buscar} son de {total_de_episodios_por_genero} episodios")

def buscar_series_por_rango_de_precio(precio_minimo,precio_maximo):
    lista_de_series_encontradas = []
    for codigo_serie,datos_de_anime in catalogo.items():
        
        precio_actual = datos_de_anime[IDX_PRECIO]
        episodios_actuales = datos_de_anime[IDX_EPISODIOS]
        
        precio_dentro_del_rango = precio_minimo<=  precio_actual <= precio_maximo
        tiene_episodios_disponibles = episodios_actuales > 0
        
        if precio_dentro_del_rango and tiene_episodios_disponibles:
            titulo_serie = series[codigo_serie][IDX_TITULO]
            lista_de_series_encontradas.append(f"{titulo_serie}--{codigo_serie} ")
    
    if len(lista_de_series_encontradas) == 0:
        print("no se encontraron series con ese rango de precio.")
        return
    lista_de_series_encontradas.sort()
    for linea in lista_de_series_encontradas:
        print(linea)

 
def actualizar_precio_de_serie(codigo, nuevo_precio):
    codigo = codigo.upper()
    if codigo in catalogo:
        catalogo[codigo][IDX_PRECIO] = nuevo_precio
        return True
    return False

def validar_texto_no_vacio(texto):
    return texto.strip() != "" 

def validar_clasificacion(clasificacion):
    return clasificacion.upper() in ("G","PG","M")

def validar_si_tiene_subtitulos(respuesta):
    return respuesta.lower()in ("s","n")

def validar_precio(precio):
    return isinstance(precio, int) and precio > 0

def validar_episodios(episodios):
    return isinstance(episodios, int) and episodios >= 0

def agregar_Serie(codigo,titulo,genero,estudio,calsificaion,subtitulado,pais,precio,episodios):
    codigo = codigo.upper()
    if codigo in series:
        return False
    series[codigo] = [titulo,genero,estudio,calsificaion,subtitulado,pais]
    catalogo[codigo] = [precio,episodios]
    return True

def Eliminar_serie(codigo):
    codigo = codigo.upper()
    if codigo in series:
        del series[codigo]
        del catalogo[codigo]
        return True
    return False
 

def mostrar_menu():
    print("\n========== MENU PRINCIPAL ==========")
    print("1. Episodios por genero")
    print("2. Busqueda de series por rango de precio")
    print("3. Actualizar precio de serie")
    print("4. Agregar serie")
    print("5. Eliminar serie")
    print("6. Salir")
    print("=====================================")
  
def ejecutar_menu():
    ejecutar_programa = True
    while ejecutar_programa:
        mostrar_menu()
        opcion_seleccionada = (input("que opcion deseas escojer "))
        
        if opcion_seleccionada == "1":
            genero_a_buscar = input("que genero buscar? ")
            contar_episodios_por_genero(genero_a_buscar)
        
        elif opcion_seleccionada == "2":
           datos_ingresados_correctamente = False
           while not datos_ingresados_correctamente:
                try:

                    print("tienes que poner tu rango de precio")
                    precio_minimo = int(input("cual es el precio minimo? "))
                    precio_maximo = int(input("cual es el precio maximo? "))
                    if precio_minimo < 0 or precio_maximo < 0:
                        print("los precvios no pueden ser negativos")
                    else:
                        datos_ingresados_correctamente = True
                except ValueError:
                 print("tiene que ser numero entero y mayor a 0")
                
           buscar_series_por_rango_de_precio(precio_minimo,precio_maximo)
        elif opcion_seleccionada == "3":
            seguir_actualizando = True
            while seguir_actualizando:
             codigo_ingresado = input("cual es el id del anime? ")
             try:
                precio_nuevo = int(input("cual es el nuevo precio que le quieres poner? "))
                if precio_nuevo <= 0:
                    print("tiene que ser un numero mayor a 0")
                else:
                    actualizacion_exitosa = actualizar_precio_de_serie(codigo_ingresado,precio_nuevo)
                    if actualizacion_exitosa:
                        print("datos actualizados")
                    else:
                     print("datos no encontrados")
             except:
                 print("tiene que ser numero entero y mayor a 0")
             respuesta = input("deseas actualizar otro precio (s/n)? ")
             if respuesta.lower() != "s":
                    seguir_actualizando = False
        elif opcion_seleccionada == "4":
            # validar las series
            codigo_nuevo = input("codigo: ")
            titulo_nuevo = input("titulo: ")
            genero_nuevo = input("genero nuevo:")
            estudio_nuevo = input("estudio: ")
            clasificacion_nueva = input("clasificacion(G/PG/M): ")
            respuesta_subtitulado = input(" esta subtitulado? (s/n)")
            pais_nuevo = input("pais de origen: ")

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
            if not validar_si_tiene_subtitulos(respuesta_subtitulado):
                print("Debe responder s o n.")
                datos_validos = False
            if not validar_texto_no_vacio(pais_nuevo):
                print("El pais no puede estar vacio.")
                datos_validos = False
            # validar el catalogo
            try:
                precio_nuevo = int(input("cual es su precio? "))
                episodios_nuevos = int(input("cuantos episodios tiene? "))
                if not validar_precio(precio_nuevo):
                    print("precion no valido")
                    datos_validos = False
                if not validar_episodios(episodios_nuevos):
                    print("episodios no validos")
                    datos_validos = False
            except ValueError:
                print("error en la informacion ingresada")
                datos_validos = False

            if datos_validos:
                subtitulado_booleano = respuesta_subtitulado.lower() == "s"
                agregado_exitoso = agregar_Serie(
                    codigo_nuevo, titulo_nuevo, genero_nuevo, estudio_nuevo,
                    clasificacion_nueva, subtitulado_booleano, pais_nuevo,
                    precio_nuevo, episodios_nuevos
                )
                if agregado_exitoso:
                    print("se agrego la serie exitosa mente")
                else:
                    print("el codigo ya esta ingresado")
        elif opcion_seleccionada == "5":
            codigo_a_eliminar = input("ingresa el codigo del anime que deseas eliminar: ")
            eliminacion_exitosa = Eliminar_serie(codigo_a_eliminar)
            if eliminacion_exitosa:
                print("serie eliminada correctamente")
            else:
                print("erro en la informacion entregada intente de nuevo")
        
        elif opcion_seleccionada == "6":
            print("hasta pronto")
            ejecutar_programa = False
        
        else:
            print("eliga una de las 6 opciones")

ejecutar_menu()


