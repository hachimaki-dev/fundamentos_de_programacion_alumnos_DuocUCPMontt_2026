# Variables iniciales (usando nombres claros y en minúsculas por buena práctica)
tecnicos_maestros = 0
tecnicos_operarios = 0

# --- HOJA 1 ---
while True:
    try:
        # Usamos comillas rectas ""
        registro = int(input("Ingrese cantidad registros: "))
        if registro <= 0:
            print("Solo puede ser mayor a 0")
            continue
        break # El break va aquí, al mismo nivel de 'registro' si no hubo error
    except ValueError:
        print("Solo puede ingresar números enteros")
        continue

print(f"Iniciando registro de {registro} técnicos")

for i in range(registro):
    print(f"Iniciando registro de técnico {i + 1}")
    
    # Bucle para el código
    while True:
        codigo = input("Ingrese código para técnico, más de 6 dígitos: ")
        if len(codigo) < 6: # < 6 detecta si es muy corto
            print("Código inválido, debe tener mínimo 6 dígitos")
        elif " " in codigo:
            print("El código no puede tener espacios")
        else:
            break

    # --- HOJA 2 (Ahora metida correctamente dentro del For) ---
    while True:
        try:
            anos_exp = int(input("Ingrese años experiencia: "))
            if anos_exp < 0:
                print("No puede ser menor a 0")
                continue
            break
        except ValueError:
            print("Solo números enteros")
            
    # Clasificación oficial del enunciado (Más de 10 o <= 10)
    if anos_exp > 10:
        tecnicos_maestros += 1
    else:
        tecnicos_operarios += 1

# El print final va completamente afuera de todos los bucles
print(f"La planta cuenta con {tecnicos_maestros} Técnicos Maestros y {tecnicos_operarios} Técnicos Operarios. Sistema listo.")