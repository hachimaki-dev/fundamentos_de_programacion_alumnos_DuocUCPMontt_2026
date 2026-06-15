senior = []
junior = []
while True:
    try:
        cantidad_ingenieros = int(input("¿Cuántos ingenieros deseas registrar?"))
        if cantidad_ingenieros > 0:
            break
        else:
            print("¡Dato inválido! Ingresa un entero positivo para continuar el registro.")
    except ValueError:
        print("¡Dato inválido! Ingresa un entero positivo para continuar el registro.")
for ingeniero in range(cantidad_ingenieros):
    while True:
        codigo_ingeniero = input("Ingresa el alias del ingeniero: ")
        if len(codigo_ingeniero) >= 6 and " " not in codigo_ingeniero:
            break
        else:
            print("Alias inválido. Debe tener al menos 6 caracteres, sin espacios y solo letras o numeros")
    while True:
        try:
            nivel_tecnico = int(input("Ingresa el nivel técnico del ingeniero: "))
            if nivel_tecnico > 0:
                if nivel_tecnico > 45:
                    senior.append({"codigo":codigo_ingeniero,"nivel":nivel_tecnico})
                    print(f"Ingeniero {codigo_ingeniero} registrado como Senior (nivel {nivel_tecnico})")
                    break
                else:
                    junior.append({"codigo":codigo_ingeniero,"nivel":nivel_tecnico})
                    print(f"Ingeniero {codigo_ingeniero} registrado como Senior (nivel {nivel_tecnico})")
                    break
            else:
                print("¡Error de validación! Ingresa un número entero positivo para el nivel técnico.")
        except ValueError:
            print("¡Error de validación! Ingresa un número entero positivo para el nivel técnico.")
print(f"¡El instituto cuenta con {len(senior)} Ingenieros Senior y {len(junior)} Ingenieros Junior! ¡Registro completado satisfactoriamente!")
print(senior)
print(junior)