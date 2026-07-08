# Diccionarios globales con la nueva temática del Mundial
coleccionistas = {
    'COL01': ['Camila Rojas', 'equipos'],
    'COL02': ['Lucas Perez',  'estadios'],
    'COL03': ['Sofia Silva',  'figuras'],
}

progreso_album = {
    'COL01': [35, 13],  # [Láminas Pegadas, Láminas Repetidas]
    'COL02': [20,  0],  
    'COL03': [55, 12],  
}

def mostrar_menu():
    print("\n========== MENÚ ÁLBUM MUNDIAL ==========")
    print("1. Total de repetidas por sección favorita")
    print("2. Búsqueda de coleccionistas por rango de pegadas")
    print("3. Actualizar láminas pegadas")
    print("4. Registrar coleccionista")
    print("5. Eliminar coleccionista")
    print("6. Salir")
    print("========================================")

def validar_opciones_del_usuario():
    while True:
        opcion_usuario_ingresada = input("Ingrese una opcion: ")
        if opcion_usuario_ingresada in ["1","2","3","4","5","6"]:
            return opcion_usuario_ingresada
        else:
            print("Debe seleccionar una opción válida")

def validar_nombre():
    while True:
        nombre = input("Ingrese nombre del coleccionista: ")
        if not nombre.strip():
            print("Nombre no valido")
        else:
            return nombre.strip()

def validar_seccion():
    while True:
        seccion = input("Ingrese seccion favorita (equipos/estadios/figuras): ").strip().lower()
        if seccion in ["equipos", "estadios", "figuras"]:
            return seccion
        else:
            print("Seccion no valida")

def validar_laminas_pegadas():
    while True:
        try:
            pegadas = int(input("Ingrese cantidad de laminas pegadas (Max 60): "))
            if pegadas < 0 or pegadas > 60:
                print("Ingrese un numero entre 0 y 60")
            else:
                return pegadas
        except ValueError:
            print("Valor invalido, ingrese un numero entero positivo")

def validar_laminas_repetidas():
    while True:
        try:
            repetidas = int(input("Ingrese cantidad de laminas repetidas: "))
            if repetidas >= 0:
                return repetidas
            else:
                print("Ingrese un numero mayor o igual a cero")
        except ValueError:
            print("Valor invalido, debe ingresar un numero entero positivo")

# OPCIÓN 1: Lógica idéntica a tu conteo de episodios por género
def cantidad_repetidas_por_seccion(validar_seccion):
    cantidad_repetidas = 0
    seccion_buscada = validar_seccion.strip().lower()
    
    for cada_coleccionista in coleccionistas.items():
        if cada_coleccionista[1][1] == seccion_buscada:
            for cada_progreso in progreso_album.items():
                if cada_progreso[0] == cada_coleccionista[0]:
                    cantidad_repetidas += cada_progreso[1][1] # Suma las repetidas
    return cantidad_repetidas

lista_de_rango_pegadas = []

# OPCIÓN 2: Lógica idéntica a tu filtrado por rango de precios
def busqueda_coleccionista_por_rango_pegadas(pegadas_min, pegadas_max):
    # Limpiamos la lista al iniciar la búsqueda para que no acumule búsquedas viejas
    lista_de_rango_pegadas.clear()
    
    for cada_progreso in progreso_album.items():
        if cada_progreso[1][0] >= pegadas_min and cada_progreso[1][0] <= pegadas_max:
            for cada_coleccionista in coleccionistas.items():
                if cada_coleccionista[0] == cada_progreso[0]:
                    datos_lista = cada_coleccionista[1][0] + "---" + cada_coleccionista[0]
                    lista_de_rango_pegadas.append(datos_lista)
                    lista_de_rango_pegadas.sort()
    return lista_de_rango_pegadas

def validar_codigo():
    while True:
        codigo = input("Ingrese codigo de coleccionista (ej: COL01): ").strip().upper()
        return codigo

def validar_nuevas_pegadas():
    while True:
        try:
            nuevas_pegadas = int(input("Ingrese nueva cantidad de pegadas: "))
            if nuevas_pegadas < 0 or nuevas_pegadas > 60:
                print("Ingrese un numero entre 0 y 60")
            else:
                return nuevas_pegadas
        except ValueError:
            print("Valor invalido, ingrese un numero entero positivo")

# OPCIÓN 3: Lógica idéntica a tu actualización de precios
def actualizar_laminas_pegadas():
    while True:
        codigo_ingresado = validar_codigo()
        
        # Verificar si el código existe en el diccionario antes de avanzar
        if codigo_ingresado not in progreso_album:
            print("Codigo invalido, no existe en los registros.")
            continuar = input("¿Desea intentar con otro codigo? s/n: ").strip().lower()
            if continuar == "n":
                break
            continue
            
        nuevas_pegadas = validar_nuevas_pegadas()
        
        for cada_progreso in progreso_album.items():
            if cada_progreso[0] == codigo_ingresado:
                cada_progreso[1][0] = nuevas_pegadas
                print("Laminas pegadas actualizadas con éxito.")
                
        continuar = input("¿Desea actualizar otro coleccionista? s/n: ").strip().lower()        
        if continuar != "s":
            break

# OPCIÓN 4: Lógica idéntica a tu función de agregar
def registrar_coleccionista():
    codigo_validado = validar_codigo()
    
    if codigo_validado in coleccionistas:
        print("Este codigo ya existe")
        return

    nombre_validado = validar_nombre()
    seccion_validado = validar_seccion()
    pegadas_validado = validar_laminas_pegadas()
    repetidas_validado = validar_laminas_repetidas()

    print(f"\nDatos recibidos: Código {codigo_validado}, Nombre {nombre_validado}, Sección Favorita {seccion_validado}, Pegadas {pegadas_validado}, Repetidas {repetidas_validado}")

    # Guardar usando asignación directa en los diccionarios globales
    coleccionistas[codigo_validado] = [nombre_validado, seccion_validado]
    progreso_album[codigo_validado] = [pegadas_validado, repetidas_validado]
    
    print("¡Coleccionista registrado con éxito!")

# OPCIÓN 5: Lógica idéntica a tu función de eliminar
def eliminar_coleccionista():
    codigo_eliminar = validar_codigo()
    if codigo_eliminar in coleccionistas:
        coleccionistas.pop(codigo_eliminar)
        progreso_album.pop(codigo_eliminar)
        print("Coleccionista eliminado correctamente.")
        return True
    else:
        print("El código no existe.")
        return False

def main():
    while True:
        mostrar_menu()
        opcion_seleccionada = validar_opciones_del_usuario()

        if opcion_seleccionada == "1":
            sec = validar_seccion()
            total_rep = cantidad_repetidas_por_seccion(sec)
            print(f"Total de láminas repetidas para la sección favorita '{sec}': {total_rep}")
            
        elif opcion_seleccionada == "2":
            try:
                p_min = int(input("Ingrese mínimo de láminas pegadas: "))
                p_max = int(input("Ingrese máximo de láminas pegadas: "))
                resultados = busqueda_coleccionista_por_rango_pegadas(p_min, p_max)
                if resultados:
                    print("\n--- Coleccionistas encontrados ---")
                    for c in resultados:
                        print(c)
                else:
                    print("No se encontraron coleccionistas en ese rango.")
            except ValueError:
                print("Debe ingresar números válidos.")
                
        elif opcion_seleccionada == "3":
            actualizar_laminas_pegadas()
        elif opcion_seleccionada == "4":
            registrar_coleccionista()
        elif opcion_seleccionada == "5":
            eliminar_coleccionista()
        elif opcion_seleccionada == "6":
            print("¡Gracias por coleccionar con nosotros! Hasta la próxima.")
            break

main()