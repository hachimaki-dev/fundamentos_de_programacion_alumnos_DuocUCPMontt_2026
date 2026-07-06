while True:
    try:
        cantidad = int(input("¿Cuántos voluntarios registrar?: "))
        if cantidad > 0:
            break
        else:
            print("debe ser mayor a 0.")
    except ValueError:
        print("Ingresa un número entero válido.")

voluntarios = []
dedicados = 0
casuales = 0

for i in range(cantidad):
    while True:
            nombre = input("Ingrese nombre: ")
            if len (nombre) >= 4 and " " not in nombre and nombre.isalnum():
                break
            else:
                print("Codigo inválido. Mínimo 4 caracteres, sin espacios y alfanumérico.")
    while True:
        try:
            horas = int(input("Horas disponibles por semana: "))
            if horas > 0:
                break
            else:
                print("Las horas deben ser mayor a 0.")
        except ValueError:
            print("Ingresa un número entero válido.")

    if horas > 20:
        categoria = "Voluntario dedicado"
        dedicados += 1
    else:
        categoria = "Voluntario Casual"
        casuales += 1
    
    vol = {"nombre": nombre, "horas": horas, "categoria": categoria}
    voluntarios.append(vol)

print(f"\n La ONG tiene {dedicados} Voluntarios Dedicados y {casuales} Voluntarios Casuales. ¡Gracias por su apoyo!.")