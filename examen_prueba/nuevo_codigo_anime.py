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

def mostrar_menu_usuario():
    print("1. Episodios por género")
    print("2. Búsqueda de series por rango de precio")
    print("3. Actualizar precio de serie")
    print("4. Agregar serie")
    print("5. Eliminar serie")
    print("6. Salir")

def validar_seleccion_usuario():
    while True:
        seleccion_usuario = input("Seleccione una opcion: ")
        if seleccion_usuario in ["1","2","3","4","5","6"]:
            return seleccion_usuario
        else:
            print("La opcion seleccionada no es valida.")

def validar_titulo():
    while True:
        titulo = input("Ingrese titulo: ")
        if not titulo.strip():
            print("Ingrese un titulo valido.")
        else:
            return titulo.strip()

def validar_genero():
    while True:
        genero = input("Ingrese genero: ")
        if not genero.strip():
            print("Ingrese genero valido.")
        else:
            return genero.strip()

def validar_estudio():
    while True:
        estudio = input("Ingrese estudio: ")
        if not estudio.strip():
            print("Ingrese un estudio valido.")
        else:
            return estudio.strip()

def validar_clasificacion():
    while True:
        clasificacion = input("Ingrese clasificacion ('G', 'PG', 'M'): ").strip().upper()
        if clasificacion in ["G","PG","M"]:
            return clasificacion
        else:
            print("Ingrese una clasificacion valida.")

def validar_subtitulo():
    while True:
        subtitulo = input("¿Tiene subtitulo? S/N: ").strip().upper()
        if subtitulo == "S":
            return True
        elif subtitulo == "N":
            return False
        else:
            print("Ingrese un subtitulo valido.")

def validar_pais_origen():
    while True:
        pais_origen = input("Ingrese pais de origen: ")
        if not pais_origen.strip():
            print("Ingrese un pais de origen valido.")
        else:
            return pais_origen.strip()

def validar_precio_mensual():
    while True:
        try:
            precio_mensual = int(input("Ingrese precio mensual: "))
            if precio_mensual > 0:
                return precio_mensual
            else:
                print("Ingrese un precio mensual valido.")
        except ValueError:
            print("Valor invalido, debe ingresar un numero entero positivo.")

def validar_episodios():
    while True:
        try:
            episodios = int(input("Ingrese episodios: "))
            if episodios >= 0:
                return episodios
            else:
                print("Ingrese una cantidad de episodios valida.")
        except ValueError:
            print("Valor invalido, debe ingresar un numero entero positivo.")

def validar_precio_minimo():
    while True:
        try:
            precio_minimo = int(input("Ingrese precio minimo: "))
            if precio_minimo >= 0:
                return precio_minimo
            else:
                print("Ingrese un precio minimo valido.")
        except ValueError:
            print("Valor invalido, debe ingresar un numero entero positivo.")

def validar_precio_maximo():
    while True:
        try:
            precio_maximo = int(input("Ingrese precio maximo: "))
            if precio_maximo > 0:
                return precio_maximo
            else:
                print("Ingrese un precio maximo valido.")
        except ValueError:
            print("Valor invalido, debe ingresar un numero entero positivo.")

def validar_nuevo_precio():
    while True:
        try:
            nuevo_precio = int(input("Ingrese nuevo precio: "))
            if nuevo_precio > 0:
                return nuevo_precio
            else:
                print("Ingrese un nuevo precio valido.")
        except ValueError:
            print("Valor invalido, debe ingresar un numero entero valido.")

def validar_codigo():
    while True:
        codigo = input("Ingrese codigo: ")
        if not codigo.strip().upper():
            print("Ingrese un codigo valido.")
        else:
            return codigo.strip().upper()
        
def buscar_episodios_por_genero(validar_genero):
    cantidad_episodios = 0
    genero_buscar = validar_genero.strip().lower()
    genero_encontrado = False

    for cada_serie in series.items():
        if cada_serie[1][1] == genero_buscar:
            genero_encontrado = True
            for cada_serie_en_catalogo in catalogo.items():
                if cada_serie[0] == cada_serie_en_catalogo[0]:
                    cantidad_episodios += cada_serie_en_catalogo[1][1]
    if genero_encontrado:
        print(f"Total episodios para el género '{validar_genero}': {cantidad_episodios}")
    else:
        print(f"No se encontraron series para el género '{validar_genero}'.")

def validar_busqueda_por_rango_precio(precio_minimo, precio_maximo):
    lista_de_rango_precio = []

    for cada_precio in catalogo.items():
        if cada_precio[1][0] >= precio_minimo and cada_precio[1][0] <= precio_maximo and cada_precio [1][1]:
            for cada_serie in series.items():
                if cada_serie[0] == cada_precio[0]:
                    datos_lista_rango_precio = cada_serie[1][0] + "--" + cada_serie[0]
                    lista_de_rango_precio.append(datos_lista_rango_precio)
    if lista_de_rango_precio:
        lista_de_rango_precio.sort()
        print("Serie encontrada")
        for serie in lista_de_rango_precio:
            print(serie)
    else:
        print("Error: No se encontraron series en ese rango de precio.")

def actualizar_precio_serie(codigo, nuevo_precio):
    if codigo in catalogo:
        catalogo[codigo][0] = nuevo_precio
        return True
    else:
        return False

def agregar_serie():
    codigo_validado = validar_codigo()

    if codigo_validado in series:
        print("Este codigo ya existe")
        return

    titulo_validado = validar_titulo()
    genero_validado = validar_genero()
    estudio_validado = validar_estudio()
    clasificacion_validado = validar_clasificacion()
    subtitulo_validado = validar_subtitulo()
    pais_origen_validado = validar_pais_origen()
    precio_validado = validar_precio_mensual()
    episodios_validados = validar_episodios()

    series[codigo_validado] = [titulo_validado, genero_validado.lower(), estudio_validado, clasificacion_validado, subtitulo_validado, pais_origen_validado,]
    catalogo[codigo_validado] = [precio_validado, episodios_validados]

    print(f"Se agrego con exito la serie {titulo_validado} con codigo {codigo_validado}")

def eliminar_serie():
    codigo_eliminar = validar_codigo()

    if codigo_eliminar in series:
        series.pop(codigo_eliminar)
        catalogo.pop(codigo_eliminar)
        print("Serie eliminada correctamente.")
        return True
    else:
        print("El codigo a eliminar no existe.")
        return False
    
def main():
    while True:
        mostrar_menu_usuario()
        opcion_seleccionada = validar_seleccion_usuario()

        if opcion_seleccionada == "1":
            genero_a_buscar = validar_genero()
            buscar_episodios_por_genero(genero_a_buscar)

        elif opcion_seleccionada == "2":
            try:
                precio_minimo = validar_precio_minimo()
                precio_maximo = validar_precio_maximo()
                validar_busqueda_por_rango_precio(precio_minimo, precio_maximo)
            except ValueError:
                print("Valor invalido, debe ingresar un numero entero positivo")

        elif opcion_seleccionada == "3":
            while True:
                codigo_a_buscar = validar_codigo()
                precio_nuevo = validar_nuevo_precio()
                if actualizar_precio_serie(codigo_a_buscar, precio_nuevo):
                    print(f"Precio actualizado correctamente con codigo {codigo_a_buscar} y nuevo precio {precio_nuevo}")
                else:
                    print("El codigo no existe.")
                
                continuar_usuario = input("¿Desea actualizar otro precio? S/N: ").strip().upper()
                if continuar_usuario != "S":
                    break
        
        elif opcion_seleccionada == "4":
            agregar_serie()
        
        elif opcion_seleccionada == "5":
            eliminar_serie()
        
        elif opcion_seleccionada == "6":
            print("Saliendo del programa")
            break

main()