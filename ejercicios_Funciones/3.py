lista_veterinaria = []
def mostrar_menu():
    print("1. Registrar animal")
    print("2. Buscar animal")
    print("3. Eliminar animal")
    print("4. Actualizar alertas")
    print("5. Mostrar animales")
    print("6. Salir")
    print("7. Insertar lista prueba")
def leer_opcion_menu():
    while True:
        opcion_ingresada = input("Ingrese una opcion: ")
        if opcion_ingresada in ["1","2","3","4","5","6","7"]:
            return opcion_ingresada
        else:
            print("Opcion invalida")
def validar_nombre():
    nombre = input("Ingrese nombre: ")
    if len(nombre) <= 0 or " " in nombre:
        print("El nombre no es valido")
    else:
        return nombre
def validar_especie():
    especie = input("Ingrese especie: ")
    if len(especie) <= 0 or " " in especie and especie:
        print("La especie no es valida")
    else:
        return especie
def validar_peso():
    while True:
        try:
            peso = int(input("Ingrese peso: "))
            if peso <= 0:
                print("Ingrese peso valido")
            else:
                return peso
        except ValueError:
            print("Valor invalido, ingrese numeros enteros positivos")
def registrar_animal():
    nombre_validado = validar_nombre()
    especie_validada = validar_especie()
    peso_validada = validar_peso()
    print(f"El nombre es {nombre_validado}, la especie es {especie_validada} y el peso es {peso_validada}")

    datos_diccionario_veterinaria = {
        "nombre": nombre_validado,
        "especie": especie_validada,
        "peso": peso_validada,
        "estado": False
    }
    lista_veterinaria.append(datos_diccionario_veterinaria)
def buscar_animal(nombre_animal_a_buscar):
    for cada_animal in lista_veterinaria:
        if cada_animal["nombre"]==nombre_animal_a_buscar:
            print("Existe")
            indice = lista_veterinaria.index(cada_animal)
            return indice
def eliminar_animal(nombre_animal_a_buscar):
    indice_encontrado_animal = buscar_animal(nombre_animal_a_buscar)
    if indice_encontrado_animal is not None:
        lista_veterinaria.pop(indice_encontrado_animal)
        return True
def actualizar_alertas():
    for cada_animal in lista_veterinaria:
        if cada_animal["peso"] <3.0:
            cada_animal["estado"] = True
def insertar_datos_pruebas():
    lista_veterinaria.append({
        "nombre": "Perro",
        "especie": "canino",
        "peso": 10,
        "estado": False
    })
    lista_veterinaria.append({
        "nombre": "Gato",
        "especie": "felino",
        "peso": 2,
        "estado": True
    })
def mostrar_toda_la_lista():
    print(lista_veterinaria)
def main():
    while True:
        mostrar_menu()
        opcion_elegida = leer_opcion_menu()

        if opcion_elegida == "1":
            registrar_animal()
        elif opcion_elegida == "2":
            buscar_nombre_animal = input("Ingrese nombre a buscar: ")
            indice_encontrado = buscar_animal(buscar_nombre_animal)

            if indice_encontrado is not None:
                print("Lo encontramos")
                print(f"Nombre: {lista_veterinaria[indice_encontrado]["nombre"]}")
                print(f"Especie: {lista_veterinaria[indice_encontrado]["especie"]}")
                print(f"Peso: {lista_veterinaria[indice_encontrado]["peso"]}")
                print(f"Estado: {lista_veterinaria[indice_encontrado]["estado"]}")
            else:
                print("No hay datos de este animal")
        elif opcion_elegida == "3":
            nombre_animal_a_eliminar = input("Ingrese nombre a eliminar: ")
            eliminado = eliminar_animal(nombre_animal_a_eliminar)
            if eliminado is not None:
                print("Se elimino exitosamente")
            else:
                print("No se puede eliminar este animal")
        elif opcion_elegida == "4":
            actualizar_alertas()
        elif opcion_elegida == "5":
            mostrar_toda_la_lista()
        elif opcion_elegida == "6":
            print("Gracias por usar el sistema. ¡Hasta pronto!")
            break
        elif opcion_elegida == "7":
            insertar_datos_pruebas()
main()