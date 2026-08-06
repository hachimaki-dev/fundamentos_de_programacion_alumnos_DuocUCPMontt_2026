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

def menu():
    while True:
        print("========== MENÚ PRINCIPAL ==========")
        print("1. Episodios por género")
        print("2. Búsqueda de series por rango de precio")
        print("3. Actualizar precio de serie")
        print("4. Agregar serie")
        print("5. Eliminar serie")
        print("6. Salir")
        print("=====================================")
        opcion_usuario = input("ingresa una opcion del 1 al 6: ").strip()
        if opcion_usuario in ["1","2","3","4","5","6"]:
            return opcion_usuario
        else:
            print("Debe seleccionar una opción válida")

def episodios_genero(genero):
    tota_episodios = 0
    for cada_serie in series.items():
        if cada_serie[1][1] == genero:
            for codigo_catalogo in catalogo.items():
                if cada_serie[0] == codigo_catalogo[0]:
                    tota_episodios += codigo_catalogo[1][1]
        
    print(f"{tota_episodios}")

def busqueda_precio(p_min, p_max):
    lista = []
    precio_minimo = p_min
    precio_maximo = p_max
    for codigo_serie,datos_catalogo in catalogo.items():
        precio_serie = datos_catalogo[0]
        episodios = datos_catalogo[1]
        if precio_minimo <= precio_serie <= precio_maximo and episodios >0:
            nombre_serie = series[codigo_serie][0]
            formato_imprecion = f"{nombre_serie}--{codigo_serie}"
            lista.append(formato_imprecion)
    if len(lista)>0:
        lista.sort()#para ordenar los datos de manera alfabetica
        for datos in lista:
            print(datos)
    else:
        print("error, no existe serie en ese rango de precio")

def actualizar_precio(codigo, nuevo_precio):
    if codigo in catalogo:
        catalogo[codigo][0] = nuevo_precio
        return True
    else:
        return False
        

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

def eliminar_serie(codigo):
    if codigo in catalogo:
        del series[codigo]
        del catalogo[codigo]
        print("encontrado")
        return True
    return False

def iniciar_programa():
    while True:
        opcion_elejida = menu()
        if opcion_elejida == "1":
            while True:
                genero_usuario = input("ingresa el genero del anime : ").strip().lower()
                if len(genero_usuario)>0:
                    episodios_genero(genero_usuario)
                    break
                else:
                    print("el apartado no puede estar vacio")

        elif opcion_elejida == "2":
            while True:
                try:
                    p_min = int(input("ingresa el precio minimo : "))
                    p_max = int(input("ingresa el precio maximo : "))
                    if p_min >=0 and p_max >=0:
                        if p_min < p_max:
                            busqueda_precio(p_min, p_max)
                            break
                        else:
                            print("el precio minimo no puede ser mayor el precio maximo")
                    else:
                        print("el precio minimo y maximo no pueden ser menor que 0")
                except ValueError:
                    print("ingresa un numero entero")

        elif opcion_elejida == "3":
            while True:
                codigo_usuario = input("ingresa el codigo del anime que desea cambiar: ").strip().upper()
                if len(codigo_usuario)>0:
                    if codigo_usuario in catalogo:
                        try:
                            usuario_nuevo_precio = int(input("ingresa el nuevo precio: "))
                            if usuario_nuevo_precio >=0:
                                actualizar_precio(codigo_usuario, usuario_nuevo_precio)
                                
                            else:
                                print("el nuevo precio no puede ser un numero menor que 0")
                        except ValueError:
                            print("ingresa un numero entero")
                    else:
                        print("el codigo ingresado no exite") 
                repetir = input("¿Desea actualizar otro precio (s/n)? ").strip().lower()
                if repetir != "s":
                    break
                      

        elif opcion_elejida == "4":
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

        elif opcion_elejida == "5":
            while True:
                codigo_para_eliminar = input("ingresa el codigo a eliminar : ").upper().strip()
                if len(codigo_para_eliminar)>0:
                    if codigo_para_eliminar in catalogo:
                        eliminar_serie(codigo_para_eliminar)
                        break
                    else:
                        return False

        elif opcion_elejida == "6":
            break
            
iniciar_programa()
