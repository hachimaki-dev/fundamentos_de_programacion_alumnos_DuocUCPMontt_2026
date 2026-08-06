animes_filtrados_por_rango_de_precio = []
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

def mostrar_menu():
    while True:
        print("===== MENÚ PRINCIPAL =====\n1. Episodios por género\n2. Busqueda de series por rango de precio\n3. Actualizar precio\n4. Agregar serie\n5. Eliminar serie\n6. Salir")
        opcion_elegida = opcion_usuario()
        if opcion_elegida == None:
            continue
        elif opcion_elegida == 6:
            print("Gracias por usar el servicio")
            break

        menu_usuario(opcion_elegida)

def opcion_usuario():
    while True:
        try:
            opcion_usuario = int(input("Ingresa tu elección: "))

            if opcion_usuario not in [1, 2, 3, 4, 5, 6]:
                print("Ingresa una de las 6 opciones disponibles.")
                return None
            else:
                return opcion_usuario
        except ValueError:
            print("Ingresa un valor valido")
            return None


def episodios_genero():
    total_episodios = 0
    nombre_genero = input("Ingresa el nombre del género que buscas: ").lower()
    if len(nombre_genero) < 1:
        print("Ingresa un género valido")
    else:
        encontrado = False


    for serie in series.items():
        if nombre_genero == serie[1][1]:
            encontrado = True
            id_serie = serie[0]
            for episodios in catalogo.items():
                if id_serie == episodios[0]:
                    total_episodios += episodios[1][1]
                    

    if encontrado == True:
        print(f"en total hay {total_episodios} del género buscado")
                    
    else:
        print("No se ha encontrado ninguna serie de ese género.")
            

def buscar_precio_minimo():
    while True:
        try:
            precio_minimo = int(input("Ingresa el precio minimo: "))
            if precio_minimo < 0:
                print("El precio minimo no puede ser menor a 0")
            else:
                return precio_minimo
        except ValueError:
            print("Ingresa un valor valido")

def buscar_precio_maximo():
    while True:
        try:
            precio_maximo = int(input("Ingresa el precio máximo: "))
            if precio_maximo < 1:
                print("Ingresa un precio mayor a 0")
            else:
                return precio_maximo
        except ValueError:
            print("Ingresa un valor valido")

def busqueda_precio():
    precio_minimo = buscar_precio_minimo()
    precio_maximo = buscar_precio_maximo()

    if precio_minimo >= precio_maximo:
        print("El precio minimo no puede ser mayor o igual al máximo")
    
    else:
        for precio in catalogo.items():
            if precio[1][0] >= precio_minimo and precio[1][0] <= precio_maximo and precio[1][1] > 0:
                codigo = precio[0]
                for serie in series.items():
                    if serie[0] == codigo:
                        print(f"Titulo: {serie[1][0]}")
                        print(f"Código: {serie[0]}")


def solicitar_codigo():
    while True:
        codigo_solicitado = input("Ingresa el código del anime: ")
        if len(codigo_solicitado) < 1:
            print("El codigo debe tener minimo 1 caracter")
        else:
            return codigo_solicitado


def actualizar_precio():
    codigo_validado = solicitar_codigo()

    for precio in catalogo.items():
        if precio[0] == codigo_validado:
            print("se actualizara el precio")
            nuevo_precio = int(input("Ingresa el nuevo precio: "))
            precio[1][0] = nuevo_precio
            
def solicitar_codigo():
    return input("Ingresa el código del anime: ").upper()
    

def validar_codigo(codigo):
    if len(codigo) < 5 or not codigo.startswith("AN"):
        print("El código debe comenzar con AN y contener 5 caracteres.")
        return False
    else:
        return True


def solicitar_titulo():
    return input("Ingresa el titulo del anime: ")
 

def validar_titulo(titulo):
    if len(titulo) < 1 or "  " in titulo:
        print("El titulo no puede estar vacio ni contener más de 1 espacio en blanco.")
        return False
    else:
        return True

def solicitar_genero():
    return input("Ingresa el género del anime: ")

def validar_genero(genero):
    if len(genero) < 1 or " " in genero:
        print("El código no puede estar vacio ni contener espacios en blanco")
        return False
    else:
        return True

def solicitar_estudio():
    return input("Ingresa el nombre del estudio: ")

def validar_estudio(estudio):
    if len(estudio) < 1 or " " in estudio:
        print("El código no puede estar vacio ni contener espacios en blanco")
        return False
    else:
        return True

def solicitar_clasificacion():
    return input("Ingresa la clasificación: ")

def validar_clasificacion(clasificacion):
    if clasificacion in ("G", "PG", "M"):
        return True
    else:
        return False

def solicitar_subtitulado():
    return input("El anime está subtitulado?\nSi/No\n:").lower()

def validar_subtitulado(subtitulado):
    if subtitulado == "si":
        return True
    elif subtitulado == "no":
        return False
    else:
        print("Solo puedes responder si o no.")

def solicitar_pais_origen():
    return input("Ingresa el país de origen: ")

def validar_pais_origen(pais):
    if len(pais) < 1 or " " in pais:
        print("El país debe contener minimo un caracter y sin espacios en blanco.")
        return False
    else:
        return True

def solicitar_precio():
    return int(input("Ingresa el precio del anime: "))

def validar_precio(precio):
    if precio <= 0:
        print("El precio debe ser mayor a 0")
        return False
    else:
        return True


def solicitar_episodios():
    return int(input("Ingresa la cantidad de episodios que tiene este anime: "))

def validar_episodios(episodios):
    if episodios < 0:
        print("El anime no puede tener menos de 0 episodios")
        return False
    else:
        return True
def registrar_anime():
    codigo = solicitar_codigo()
    titulo = solicitar_titulo()
    genero = solicitar_genero()
    estudio = solicitar_estudio()
    clasificacion = solicitar_clasificacion()
    subtitulado = solicitar_subtitulado()
    pais = solicitar_pais_origen()
    precio = solicitar_precio()
    episodios = solicitar_episodios()


    validar_codigo(codigo)
    validar_titulo(titulo)
    validar_genero(genero)
    validar_estudio(estudio)
    validar_clasificacion(clasificacion)
    validar_subtitulado(subtitulado)
    validar_pais_origen(pais)
    validar_precio(precio)
    validar_episodios(episodios)
    print("Quiero queque")

def menu_usuario(opcion):
    if opcion == 1:
        episodios_genero()
    elif opcion == 2:
        busqueda_precio()
    elif opcion == 3:
        actualizar_precio()
    elif opcion == 4:
        registrar_anime()
    else:
        print("E")
def main():
    mostrar_menu()

main()