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

def mostrar_menu():
    print("\n========== MENÚ PRINCIPAL ==========")
    print("1. Episodios por género")
    print("2. Búsqueda de series por rango de precio")
    print("3. Actualizar precio de serie")
    print("4. Agregar serie")
    print("5. Eliminar serie")
    print("6. Salir")
    print("====================================")

def validar_opciones_del_usuario():
    while True:
        opcion_usuario_ingresada = input("Ingrese una opcion: ")
        if opcion_usuario_ingresada in ["1","2","3","4","5","6"]:
            return opcion_usuario_ingresada
        else:
            print("Debe seleccionar una opción válida")

# CORRECCIÓN: Se cambió "if titulo.strip():" por "if not titulo.strip():" (Estaba al revés)
def validar_titulo():
    while True:
        titulo = input("Ingrese titulo: ")
        if not titulo.strip():
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

# CORRECCIÓN: Se cambió "if estudio.strip():" por "if not estudio.strip():"
def validar_estudio():
    while True:
        estudio = input("Ingrese estudio: ")
        if not estudio.strip():
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

# CORRECCIÓN: Se cambió "if pais_origen.strip():" por "if not pais_origen.strip():"
def validar_pais_origen():
    while True:
        pais_origen = input("Ingrese pais de origen: ")
        if not pais_origen.strip():
            print("Pais de origen invalido")
        else:
            return pais_origen.strip()

def validar_precio():
    while True:
        try:
            precio = int(input("Ingrese precio: "))
            if precio <= 0: # CORRECCIÓN: El precio mensual debe ser mayor que cero (no incluye el 0)
                print("Ingrese un numero mayor que cero")
            else:
                return precio
        except ValueError:
            print("Valor invalido, ingrese un numero entero positivo")

def validar_precio_min():
    while True:
        try:
            precio_min = int(input("Precio minimo: "))
            if precio_min < 0:
                print("Ingrese un numero mayor o igual a cero")
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

# CORRECCIÓN: Cambiado el índice a [1][1] para apuntar correctamente al género.
# Según la rúbrica, no debe retornar valor, sino imprimir directamente en pantalla de forma case-insensitive.
def cantidad_episodios_por_genero(validar_genero):
    cantidad_episodios = 0
    genero_buscado = validar_genero.strip().lower()
    encontrado = False
    
    for cada_serie in series.items():
        if cada_serie[1][1].lower() == genero_buscado: # El índice 1 de la lista es el género
            encontrado = True
            for cada_serie_en_catalogo in catalogo.items():
                if cada_serie_en_catalogo[0] == cada_serie[0]:
                    cantidad_episodios += cada_serie_en_catalogo[1][1]
                    
    if encontrado:
        print(f"Total episodios para el género '{validar_genero}': {cantidad_episodios}")
    else:
        print(f"No se encontraron series para el género '{validar_genero}'.")

# CORRECCIÓN: Se movió la lista adentro para que se limpie en cada búsqueda.
# Se agregó el filtro de episodios > 0 que pide la imagen 3.
def busqueda_serie_por_rango_precio(precio_min, precio_max):
    lista_de_rango_precio = [] 
    for cada_precio in catalogo.items():
        # Filtra por rango de precio Y que tenga episodios > 0
        if cada_precio[1][0] >= precio_min and cada_precio[1][0] <= precio_max and cada_precio[1][1] > 0:
            for cada_serie in series.items():
                if cada_serie[0] == cada_precio[0]:
                    datos_lista = cada_serie[1][0] + "---" + cada_serie[0]
                    lista_de_rango_precio.append(datos_lista)
                    
    if lista_de_rango_precio:
        lista_de_rango_precio.sort()
        print("\n--- Series encontradas ---")
        for serie in lista_de_rango_precio:
            print(serie)
    else:
        print("Error: No se encontraron series en ese rango de precio.")

# CORRECCIÓN: Para verificar si existe un código, no necesitas iterar todo el diccionario. 
# Además, la validación del código debe pasar a mayúsculas para ser case-insensitive.
def validar_codigo():
    while True:
        codigo = input("Ingrese codigo: ").strip().upper()
        if codigo:
            return codigo
        else:
            print("Codigo invalido")

# CORRECCIÓN: Se cambió int("Ingrese...") por int(input("Ingrese...")) ya que faltaba el input.
def validar_nuevo_precio():
    while True:
        try:
            nuevo_precio = int(input("Ingrese nuevo precio: "))
            if nuevo_precio <= 0:
                print("Ingrese un numero mayor que cero")
            else:
                return nuevo_precio
        except ValueError:
            print("Valor invalido, ingrese un numero entero positivo")

# CORRECCIÓN: Se adaptó para que reciba el código y el precio, modifique los datos y retorne True/False.
# La lógica de repetir el proceso se maneja directamente desde el main() para respetar tu flujo.
def actualizar_precio(codigo, nuevo_precio):
    if codigo in catalogo:
        catalogo[codigo][0] = nuevo_precio
        return True
    return False

# CORRECCIÓN: Cambiado .append() por asignación directa de diccionarios d[c]=v.
# Corregida la sintaxis en datos_registro_catalogo (cambiada coma por dos puntos).
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
    precio_validado = validar_precio()
    episodios_validado = validar_episodios()

    # Guardar en los diccionarios globales de forma correcta
    series[codigo_validado] = [titulo_validado, genero_validado.lower(), estudio_validado, clasificacion_validado, subtitulo_validado, pais_origen_validado]
    catalogo[codigo_validado] = [precio_validado, episodios_validado]
    
    print(f"\nSe agregó con éxito la serie {titulo_validado} [{codigo_validado}]")

# CORRECCIÓN: Se eliminó el bucle 'for' que modificaba el diccionario mientras se iteraba.
# Ahora elimina directamente usando la clave si esta existe.
def eliminar_serie():
    codigo_eliminar = validar_codigo()
    if codigo_eliminar in series:
        series.pop(codigo_eliminar)
        catalogo.pop(codigo_eliminar)
        print("Serie eliminada correctamente.")
        return True
    else:
        print("El código no existe.")
        return False

def main():
    while True:
        mostrar_menu()
        opcion_seleccionada = validar_opciones_del_usuario()

        if opcion_seleccionada == "1":
            buscar_episodio_genero = validar_genero()
            cantidad_episodios_por_genero(buscar_episodio_genero)
            
        elif opcion_seleccionada == "2":
            # La rúbrica pide try/except en el programa principal para los precios mínimo y máximo
            try:
                p_min = validar_precio_min()
                p_max = validar_precio_max()
                busqueda_serie_por_rango_precio(p_min, p_max)
            except ValueError:
                print("Debe ingresar números enteros válidos.")
                
        elif opcion_seleccionada == "3":
            # Bucle para repetir la actualización si el usuario quiere
            while True:
                codigo_a_buscar = validar_codigo()
                nuevo_precio_a_actualizar = validar_nuevo_precio()
                if actualizar_precio(codigo_a_buscar, nuevo_precio_a_actualizar):
                    print("Precio actualizado correctamente.")
                else:
                    print("El código no existe en el catálogo.")
                
                continuar = input("¿Desea actualizar otro precio? s/n: ").strip().lower()
                if continuar != "s":
                    break
                    
        elif opcion_seleccionada == "4":
            agregar_serie()
        elif opcion_seleccionada == "5":
            eliminar_serie()
        elif opcion_seleccionada == "6":
            print("Saliendo del programa...")
            break

main()