# Inicialización de variables
lista_tecnicos = []
conteo_categorias = {
    "Técnico Maestro": 0,
    "Técnico Operario": 0
}

# 1. Preguntar cuántos técnicos se registrarán
while True:
    try:
        tecnicos_a_registrar = int(input("¿Cuántos técnicos se van a registrar?: "))
        if tecnicos_a_registrar <= 0:  # Validamos que no sea 0 ni negativo
            print("Tiene que ser un número entero positivo mayor a cero.")
        else:
            print(f"Se registrarán {tecnicos_a_registrar} técnicos.\n")
            break
    except ValueError:
        print("Tienes que usar un número entero positivo.")

# 2. El bucle FOR debe envolver a todo el proceso de registro
for i in range(tecnicos_a_registrar):
    print(f"--- Registro del Técnico {i + 1} ---")

    # Validación del Nombre/Código
    while True:
        try:
            nombre = input("Ingresa el código/nombre del técnico: ")
            if len(nombre) >= 6 and " " not in nombre:
                break
            else:
                print("Inválido: mínimo 6 caracteres, sin espacios.")
        except:
            print("Ocurrió un error al ingresar el nombre.")

    # Validación de Años de Experiencia
    while True:
        try:
            años_de_experiencia = int(input("¿Cuántos años de experiencia tiene?: "))
            if años_de_experiencia >= 0:
                break
            else:
                print("Los años de experiencia no pueden ser negativos.")
        except ValueError:
            print("Solo números enteros positivos.")

    # Inicializamos la variable de manera formal
    categoria = ""

    # Clasificación exacta (coincidiendo con las llaves del diccionario)
    if años_de_experiencia > 10:
        categoria = "Técnico Maestro"
    else:
        categoria = "Técnico Operario"

    # Ahora sí sumamos al contador usando la variable 'categoria'
    conteo_categorias[categoria] += 1

    # Guardamos los datos en el diccionario del técnico actual
    tecnicos = {
        "nombre": nombre,
        "experiencia": años_de_experiencia, # Corregido para que guarde los años
        "categoria": categoria
    }
    lista_tecnicos.append(tecnicos)
    print("Técnico registrado con éxito.\n")

# 3. Mostrar el resultado final (FUERA del bucle for)
print("-" * 40)
maestros = conteo_categorias["Técnico Maestro"]
operarios = conteo_categorias["Técnico Operario"]

print(f"La planta cuenta con {maestros} Técnicos Maestros y {operarios} Técnicos Operarios. Sistema listo.")





