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
    'AN006': [6990,  13],}

def mostrar_menu():
    print("1. Episodios por género")
    print("2. Búsqueda de series por rango de precio")
    print("3. Actualizar precio de serie")
    print("4. Agregar serie")
    print("5. Eliminar serie")
    print("6. Salir")

def validar_opciones_del_usuario():
    while True:
        opcion_usuario_ingresada = input("Ingrese una opcion: ")
        if opcion_usuario_ingresada in ["1","2","3","4","5","6"]:
            return opcion_usuario_ingresada
        else:
            print("Debe seleccionar una opción válida")

def validar_titulo():
    while True:
        titulo = input("Ingrese titulo: ")
        if titulo.strip():
            print("Titulo no valido")
        else:
            return titulo.strip()

def validar_genero():
    while True:
        genero = input("Ingrese genero: ")
        if not genero.strip():
            print("Genero no valido")
        else:
            return genero.strip()

def validar_estudio():
    while True:
        estudio = input("Ingrese estudio: ")
        if estudio.strip():
            print("Estudio no valido")
        else:
            return estudio.strip()

def validar_clasificacion():
    while True:
        clasificacion = input("Ingrese clasificacion: ").strip().upper()
        if clasificacion in ["G", "PG", "M"]:
            return clasificacion
        else:
            print("Clasificacion no valida")

def validar_subtitulo():
    while True:
        subtitulo = input("¿Esta subtitulado?, (S = si, N = No) : ").strip().upper()
        if subtitulo == "S":
            return True
        elif subtitulo == "N":
            return False
        else:
            print("Subtitulado no es valido")

def validar_pais_origen():
    while True:
        pais_origen = input("Ingrese pais de origen: ")
        if pais_origen.strip():
            print("Pais de origen invalido")
        else:
            return pais_origen.strip()

def validar_precio():
    while True:
        try:
            precio = int(input("Ingrese precio: "))
            if precio > 0:
                return precio
            else:
                print("Ingrese un numero mayor que cero")
        except ValueError:
            print("Valor invalido, ingrese un numero entero positivo")
def validar_precio_min():
    while True:
        try:
            precio_min = int(input("Precio minimo: "))
            if precio_min < 0:
                print("Ingrese un numero mayor que cero")
            else:
                return precio_min
        except ValueError:
            print("Valor invalido, debe ingresar un numero entero positivo")

def validar_precio_max():
    while True:
        try:
            precio_max = int(input("Precio maximo: "))
            if precio_max <= 0:
                print("Ingrese un numero mayor que cero")
            else:
                return precio_max
        except ValueError:
            print("Valor invalido, debe ingresar un numero entero positivo")

def validar_episodios():
    while True:
        try:
            episodios = int(input("Ingrese cantidad de episodios: "))
            if episodios >= 0:
                return episodios
            else:
                print("Ingrese un numero mayor o igual a cero")
        except ValueError:
            print("Valor invalido, debe ingresar un numero entero positivo")

def cantidad_episodios_por_genero(validar_genero):
    cantidad_episodios = 0
    for cada_serie in series.items():
        if cada_serie[1][1] == validar_genero:
            for cada_serie_en_catalogo in catalogo.items():
                if cada_serie_en_catalogo[0] == cada_serie[0]:
                    cantidad_episodios += cada_serie_en_catalogo[1][1]
    return cantidad_episodios

lista_de_rango_precio = []

def busqueda_serie_por_rango_precio(precio_min, precio_max):
    for cada_precio in catalogo.items():
        if cada_precio[1][0] >= precio_min and cada_precio[1][0] <= precio_max:
            for cada_serie in series.items():
                if cada_serie[0] == cada_precio[0]:
                    datos_lista = cada_serie[1][0] + "---" + cada_serie[0]
                    lista_de_rango_precio.append(datos_lista)
                    lista_de_rango_precio.sort()
    return lista_de_rango_precio

def validar_codigo():
    while True:
        codigo = input("Ingrese codigo: ")
        for cada_serie_catalogo in catalogo.items():
            if cada_serie_catalogo[0] == codigo.strip():
                return codigo.strip()
            else:
                print("Codigo invalido")

def validar_nuevo_precio():
    while True:
        try:
            nuevo_precio = int(input("Ingrese nuevo precio: "))
            if nuevo_precio < 0:
                print("Ingrese un numero mayor o igual a cero")
            else:
                return nuevo_precio
        except ValueError:
            print("Valor invalido, ingrese un numero entero positivo")

def actualizar_precio(codigo,nuevo_precio):
    while True:
        codigo()
        nuevo_precio()
        for cada_precio_catalogo in catalogo.items():
            if cada_precio_catalogo[1][0]:
                cada_precio_catalogo[1][0] = nuevo_precio()
        continuar = input("¿Desea actualizar otro precio? s/n: ")        
        if continuar == "s":
            print("todavia no la he hecho")
        elif continuar == "n":
            break

def agregar_serie():
    codigo_validado = validar_codigo()
    titulo_validado = validar_titulo()
    genero_validado = validar_genero()
    estudio_validado = validar_estudio()
    clasificacion_validado = validar_clasificacion()
    subtitulo_validado = validar_subtitulo()
    pais_origen_validado = validar_pais_origen()
    precio_validado = validar_precio()
    episodios_validado = validar_episodios()

    print(f"Se agrego codigo {codigo_validado}, se agrego titulo {titulo_validado}, se agrego genero {genero_validado}, se agrego estudio {estudio_validado}, se agrego clasificacion {clasificacion_validado}, se agrego subtitulo {subtitulo_validado}, se agrego pais origen {pais_origen_validado}, se agrego precio en catalogo {precio_validado}, se agrego episodios en catalogo {episodios_validado}")

    datos_registro_serie = {
        codigo_validado: [titulo_validado, genero_validado, estudio_validado, clasificacion_validado, subtitulo_validado, pais_origen_validado]
    }
    datos_registro_catalogo = {
        codigo_validado, [precio_validado, episodios_validado]
    }
    
    for cada_serie in series.items():
        if cada_serie[0] != codigo_validado:
            series.append(datos_registro_serie)
        else:
            print("Este codigo ya exite")
    
    for cada_serie_catalogo in catalogo.items():
        if cada_serie_catalogo[0] != codigo_validado:
            catalogo.append(datos_registro_catalogo)
        else:
            print("Este codigo ya existe")

def eliminar_serie():
    while True:
        codigo_eliminar = validar_codigo()
        for cada_serie in series.items():
            if cada_serie[0] == codigo_eliminar:
                series.pop(codigo_eliminar)
                return True

def main():
    while True:
        mostrar_menu()
        opcion_seleccionada = validar_opciones_del_usuario()

        if opcion_seleccionada == "1":
            
        elif opcion_seleccionada == "2":
            busqueda_serie_por_rango_precio()
        elif opcion_seleccionada == "3":
            actualizar_precio()
        elif opcion_seleccionada == "4":
            agregar_serie()
        elif opcion_seleccionada== "5":
            eliminar_serie()
        elif opcion_seleccionada == "6":
            break

main()
