def validar_nombre():
    while True:
        nombre_usuario = input("Ingrese su nombre: ").strip()

        if " " in nombre_usuario or nombre_usuario == "":
            print("Error: El nombre no puede estar vacío ni contener espacios.")
        else:
            return nombre_usuario
        
def validar_comuna():
    while True:
        comuna = input("Ingrese su comuna (Providencia, Maipú, Las Condes): ").strip().title()

        if comuna in ["Providencia", "Maipú", "Las Condes"]:
            return comuna
        else:
            print("Error: Comuna no válida. Intente nuevamente.")
            
def validar_metrica():
    while True:
        try:
            cantidad_errores_pagina = input("Ingrese el número de errores de interpretación en formato decimal (ej: 3.2): ")

            if "." not in cantidad_errores_pagina:
                print("Error: Ingrese un número en formato decimal válido (ej: 1.0, 2.0)")
                continue

            cantidad_errores_pagina = float(cantidad_errores_pagina)

            if cantidad_errores_pagina >= 0.0:
                return cantidad_errores_pagina
            else:
                print("Error: Ingrese un número decimal positivo válido")

        except ValueError:
            print("Error: Ingrese un número decimal válido")

def validar_test_comprension():
    while True:
        compresion = input("¿Logró explicar con sus palabras la interfaz? (si o no): ").strip().lower()

        if compresion == "si":
            return True
        elif compresion == "no":
            return False
        else:
            print("Error: Por favor responda estrictamente con un (si o no).")

def agregar_usuario(lista_general):
    print("\n--- REGISTRANDO NUEVO USUARIO TEST ---")

    nombre_valido = validar_nombre()
    comuna_valida = validar_comuna()
    metrica_valida = validar_metrica()
    compresion_valida = validar_test_comprension()

    nuevo_usuario = {
        "nombre": nombre_valido,
        "comuna": comuna_valida,
        "metrica": metrica_valida,
        "compresion": compresion_valida,    
        "rediseño_exitoso": False
    }

    lista_general.append(nuevo_usuario)
    print(f"\n¡Usuario {nombre_valido} de {comuna_valida} registrado con éxito!")



def buscar_usuario(lista_general, comuna_buscada):
    for posicion in range(len(lista_general)):
        if lista_general[posicion]["comuna"] == comuna_buscada:
            return posicion
    return -1

def eliminar_usuario(lista_general, comuna_a_eliminar):
    posicion = buscar_usuario(lista_general, comuna_a_eliminar)
    
    if posicion != -1:
        lista_general.pop(posicion)
        return True
    return False


def actualizar_estados_exito(lista_general):
    for usuario in lista_general:
        
        if usuario["metrica"] < 3.2 and usuario["compresion"] is True:
            usuario["rediseño_exitoso"] = True
        else:
            usuario["rediseño_exitoso"] = False


def mostrar_resultados_globales(lista_general):
    if len(lista_general) == 0:
        print("\nNo hay usuarios registrados para mostrar resultados.")
        return
    
    actualizar_estados_exito(lista_general)

    print("\n=== RESULTADOS DEL TEST DE USABILIDAD ===")
    for usuario in lista_general:
        comprension_str = "SÍ" if usuario["compresion"] else "NO"
        exito_str = "SÍ (Guió al usuario)" if usuario["rediseño_exitoso"] else "NO (Causó confusión)"
        
        print(f"\nNombre: {usuario['nombre']}")
        print(f"Comuna: {usuario['comuna']}")
        print(f"Errores: {usuario['metrica']}")
        print(f"Comprensión: {comprension_str}")
        print(f"Diseño Exitoso: {exito_str}")
        print("*" * 44)

def mostrar_menu():
    print(
    "\n========== MENÚ PRINCIPAL ==========\n" \
    "1. Agregar usuario test\n" \
    "2. Buscar usuario por comuna\n" \
    "3. Eliminar usuario\n" \
    "4. Actualizar estados de éxito (Línea Base)\n" \
    "5. Mostrar resultados globales\n" \
    "6. Salir")

def leer_opcion():
    while True:
        opcion_elegida = input("Seleccione una opción (1-6): ")
        if opcion_elegida.isdigit():
            numero = int(opcion_elegida)
            if 1 <= numero <= 6:
                return numero
        print("Opción inválida. Ingrese un número entre 1 y 6.")


lista_usuario_test = []

while True:
    mostrar_menu()
    opcion_elegida = leer_opcion()

    if opcion_elegida == 1:
        agregar_usuario(lista_usuario_test)

    elif opcion_elegida == 2:
        print("\n--- BUSCAR USUARIO POR COMUNA ---")
        comuna_a_buscar = validar_comuna()
        
        posicion_encontrada = buscar_usuario(lista_usuario_test, comuna_a_buscar)
        
        if posicion_encontrada != -1:
            usuario = lista_usuario_test[posicion_encontrada]
            comprension_str = "SÍ" if usuario["compresion"] else "NO"
            print(f"\n[Usuario Encontrado en Posición {posicion_encontrada}]")
            print(f"Nombre: {usuario['nombre']} | Errores: {usuario['metrica']} | Comprensión: {comprension_str}")
        else:
            print(f"No se encontraron usuarios registrados en la comuna '{comuna_a_buscar}'.")

    elif opcion_elegida == 3:
        print("\n--- ELIMINAR USUARIO ---")
        comuna_a_eliminar = validar_comuna()
        
        fue_eliminado = eliminar_usuario(lista_usuario_test, comuna_a_eliminar)
        
        if fue_eliminado:
            print(f"El usuario de la comuna '{comuna_a_eliminar}' fue eliminado con éxito.")
        else:
            print(f"El usuario de la comuna '{comuna_a_eliminar}' no se encuentra registrado.")

    elif opcion_elegida == 4:
        actualizar_estados_exito(lista_usuario_test)
        print("\n¡Estados de éxito sincronizados correctamente con la Línea Base Alpha (3.2 errores)!")

    elif opcion_elegida == 5:
        mostrar_resultados_globales(lista_usuario_test)

    elif opcion_elegida == 6:
        print("\n¡Resultados validados! El diseño centrado en el usuario ha demostrado su efectividad.")
        break`