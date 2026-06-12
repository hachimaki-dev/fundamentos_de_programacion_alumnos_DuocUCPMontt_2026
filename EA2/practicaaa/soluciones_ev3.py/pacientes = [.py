senior = 0
junior = 0

while True:

    try:
        cantidad = int(input("cuantos ingenieros desea agregar:"))

        if cantidad > 0:
            break
        else:
            print("debe ingresar un numero entero")
    except ValueError:
        print("¡Dato inválido! Ingresa un entero positivo para continuar el registro.")

for c in range(cantidad):
    while True:
        alias = input("Ingresa el alias del ingeniero:")

        try:
            if len(alias) >= 6 and " " not in alias:
                break
            else:
                print("alias invalido")
        except ValueError:
            print("Alias inválido. Debe tener al menos 6 caracteres, sin espacios y solo letras o números")
    
    while True:

        try:
            nivel = int(input("ingresa el nivel técnico del ingeniero:"))

            if nivel > 0:
                break
            else:
                print("debe ingresar un entero positivo")
        except ValueError:
            print("¡Dato inválido! Ingresa un entero positivo para continuar el registro.")

    if nivel <= 45:
        junior += 1
        print(f"{alias}: es ingeniero junior")

    else:
        senior += 1
        print(f"{alias}: es ingeniero senior")

print(f"el intituto cuenta con {senior} ingenieros senior y {junior} ingenieros junior")   
    