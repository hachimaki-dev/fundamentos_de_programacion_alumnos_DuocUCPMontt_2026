colección_de_bichos = []
def verificador_de_especie(especie):
    if len(especie) == 0:
        return False
    else: 
        return True
def verificador_tamaño(tamaño):
    try:
        tamaño = int
        if tamaño <= 0:
            print("Ingrese un tamaño mayor a 0")
        else:
            return False
    except:
        print("Ingrese")
def agregar_bicho():
    especie_del_bicho = input("Ingresar especie: ")
    if verificador_de_especie(especie_del_bicho.strip) == True:
        especie_del_bicho.strip = especie_del_bicho
    else:
        print("Ingrese una especie válida. Que no sean solo espacios vacíos.")
    tamaño_del_bicho = int(input("Ingresar tamaño: "))
    peligrosidad_del_bicho = float(input("Ingresar peligrosidad: "))
def menú_de_opciones():
    print("========== MENÚ PRINCIPAL ==========\n1. Agregar bicho\n2. Buscar bicho\n3. Eliminar bicho\n4. Actualizar estados\n5. Mostrar bichos\n6. Salir\n=====================================")
