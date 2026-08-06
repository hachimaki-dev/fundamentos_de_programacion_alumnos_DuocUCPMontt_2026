"""    catalogo = {'AN001': [9990, 75]}
    series = {'AN001': [9990, 75]}

    print(catalogo['AN001'][0])

    for codigo,valor in catalogo.items():
        for codigo_series in series:
            if codigo == codigo_series:
                pass"""

series = {
  'AN001': ['Attack on Titan',  'accion', 'MAPPA',   'M', False, 'Japon'],
  'AN002': ['Your Name',     'romance', 'CoMix Wave', 'PG', True, 'Japon'],
  'AN003': ['One Punch Man',   'comedia', 'J.C.Staff', 'PG', False, 'Japon'],
  'AN004': ['Kimetsu no Yaiba', 'accion', 'ufotable', 'PG', True, 'Japon'],
  'AN005': ['No Game No Life',  'isekai', 'Madhouse', 'PG', True, 'Japon'],
  'AN006': ['Violet Evergarden', 'drama', 'KyoAni',  'G', True, 'Japon'],
}

catalogo = {
  'AN001': [9990, 75],
  'AN002': [4990, 0],
  'AN003': [7990, 12],
  'AN004': [8990, 26],
  'AN005': [5990, 13],
  'AN006': [6990, 13],
}

def validacion_eliminacion_serie():
    serie_eliminar = input("ingresa el codigo a eliminar: ").strip().upper()
    if serie_eliminar in series:
        del series[serie_eliminar]
        del catalogo[serie_eliminar]
        print(series)
        print(catalogo)
        return serie_eliminar
    else:
        print("el codigo no existe")

def agregar_serie(codigo,titulo,genero,estudio,clasificacion,subtitulado,pais_origen,precio,episodios):
    series[codigo] = [titulo,genero,estudio,clasificacion,subtitulado,pais_origen]
    catalogo[codigo] = [precio,episodios]

def validacion_episodios():
    while True:    
        try:
            episodios = int(input("ingresa la cantidad de episodios: "))
            if episodios >=0:
                return episodios
            else:
                print("intenta nuevamente")
        except ValueError:
            print("ingresa un numero valido")

def validacion_precio():
    while True:
        try:
            precio = int(input("ingresa el precio del anime : "))
            if precio >0:
                return precio
            else:
                print("intenta nuevamente")
        except ValueError:
            print("ingresa un valor valido")
                
def validacion_pais():
    while True:
        pais_origen = input("ingresa el pais de origen : ").lower().strip()
        if len(pais_origen)>0:
            return pais_origen
        else:
            print("intenta nuevamente")

def validacion_subtitulado():
    while True:
        subtitulado = input("el anime esta subtitulado ? :\n s/n  ").strip().lower()
        if len(subtitulado)>0:
            if subtitulado in ["s","n"]:
                return subtitulado
            else:
                print("ingresa una respuesta valida: s/n")
        else:
            print("intenta nuevamente")
    
def validacion_clasificacion():
    while True:
        clasificacion = input("ingresa la clasificacion del anime : ").upper().strip()
        if clasificacion in  ["M","PG","G"]:
            return clasificacion
        else:
            print("ingresa la clasificacion correspondiente correctamente")

def validacion_estudio():
    while True:
        estudio = input("ingresa el estudio del anime : ").lower().strip()
        if len(estudio)>0:
            return estudio
        else:
            print("intenta nuevamente")

def validacion_genero():
    while True:
        genero = input("ingresa el genero del anime : ").lower().strip()
        if len(genero) > 0:
            return genero
        else:
            print("intenta nuevamente")

def validacion_titulo():
    while True:
        titulo = input("ingresa el titulo del anime : ").lower().strip()
        if len(titulo)>0:
            return titulo
        else:
            print("intenta nuevamente")

def validacion_codigo():
    while True:    
        codigo = input("ignresa el codigo de la serie : ").upper().strip()
        if len(codigo) > 0:
            if codigo not in catalogo:
                if codigo not in series:
                    return codigo
                else:
                    print("intenta nuevamente")
            else:
                print("ese codigo ya existe. intenta nuevamente") 
        else:
            print("intenta nuevamente")       
             
def actualizar_precio(codigo, nuevo_precio):
    codigo_limpio = codigo.upper()
    if codigo_limpio in catalogo:
        catalogo[codigo_limpio][0] = nuevo_precio  
        return True
    else:
        return False
            
def busqueda_precio(p_min,p_max):
    lista = []
    for codigo_serie , datos_catalogo in catalogo.items():
        precio = datos_catalogo[0]
        episodios = datos_catalogo[1]
        if p_min <= precio <= p_max and episodios >0:
            nombre_serie = series[codigo_serie][0]
            formato_imprecion = f"{nombre_serie}--{codigo_serie}"
            lista.append(formato_imprecion)
    if len(lista)>0:
        lista.sort()#para odernar los datos alfabeticamente
        for dato in lista:
            print(dato)        
    else: print("error")

def episodios_genero(busqueda_genero_usuario):
    total_episodios_genero = 0
    for codigo_series in series.items():
        if codigo_series[1][1] == busqueda_genero_usuario:
            for codigo_catalogo in catalogo.items():
                if codigo_series[0] == codigo_catalogo[0]:
                    total_episodios_genero += codigo_catalogo[1][1]
    print(f"total episodios del genero {busqueda_genero_usuario}: {total_episodios_genero}")                

def menu():
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Episodios por género")
    print("2. Búsqueda de series por rango de precio")
    print("3. Actualizar precio de serie")
    print("4. Agregar serie")
    print("5. Eliminar serie")
    print("6. Salir")
    print("=====================================")
   
def validacion_menu():
    while True:
        opcion_usuario = input("ingresa una opcion del menu 1-6 : ")
        if opcion_usuario in ["1","2","3","4","5","6"]:
            return opcion_usuario
        print("intenta una opcion valida")

def iniciar_programa():
    while True:
        menu()
        opcion_menu_elegida = validacion_menu()

        if opcion_menu_elegida == "1":
            busqueda_genero_usuario = input("ingresa el genero a buscar : ").strip()
            if len(busqueda_genero_usuario) >0:
                episodios_genero(busqueda_genero_usuario)

        elif opcion_menu_elegida == "2":
            try:
                p_min = int(input("ingresa el precio minimo: "))
                p_max = int(input("ingresa el precio maximo: "))
                if p_min >= 0 and p_max >= p_min:
                    busqueda_precio(p_min, p_max)     
            except ValueError:
                print("ingresa numeros validos")

        elif opcion_menu_elegida == "3":
            continuar = "s"
            while continuar == "s":
                codigo = input("Ingrese el código de la serie: ").strip()
                try:
                    nuevo_precio = int(input("Ingrese el nuevo precio: "))
                    if nuevo_precio < 0:
                        print("El precio no puede ser negativo.")
                    else:
                        exito = actualizar_precio(codigo, nuevo_precio)
                    if exito:
                        print("Precio modificado exitosamente.")
                    else:
                        print("Error: El código de serie no existe.")
                except ValueError:
                    print("Ingrese un número entero válido.")
                continuar = input("¿Desea actualizar otro precio (s/n)?: ").lower().strip()

        elif opcion_menu_elegida == "4":
            codigo_usuario = validacion_codigo()
            titulo_usuario = validacion_titulo()
            genero_usuario = validacion_genero()
            estudio_usuario = validacion_estudio()
            clasificacion_usuario = validacion_clasificacion()
            subtitulado_usuario = validacion_subtitulado()
            pais_usuario = validacion_pais()
            precio_usuario = validacion_precio()
            episodios_usuario = validacion_episodios()
            agregar_serie(codigo_usuario,titulo_usuario,genero_usuario,estudio_usuario,clasificacion_usuario,subtitulado_usuario,pais_usuario,precio_usuario,episodios_usuario)
            print(series)
            print(catalogo)

        elif opcion_menu_elegida == "5":
            serie_eliminar = validacion_eliminacion_serie()

        elif opcion_menu_elegida == "6":
            break

        else:
            print("ingresa una opcion valida : 1-6")
            iniciar_programa()

iniciar_programa()