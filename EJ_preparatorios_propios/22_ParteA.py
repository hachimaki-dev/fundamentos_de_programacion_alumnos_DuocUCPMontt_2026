paciente_grande = 0
paciente_pequeño = 0

print("#####"*6)
print("Clinica Veterinaria")
print("#####"*6)
print()

while True:
    try:
        animales_registrados = int(input("Ingrese cuantos animales se van a registrar :     "))
        if animales_registrados <= 0:
            print("El numero ingresado debe de ser un numero entero positivo")
        else:
            break
    except ValueError:
        print("Ingrese una opcion valida")

for a in range(animales_registrados):

    while True:
        id_animal = input("Ingrese el id de el animal :     ").upper()
        if len(id_animal) < 6 or " " in id_animal:
            print("Ingrese un id el cual tenga minimo 6 caracteres y sin espacios")
        else:
            break

    while True:
        try:
            peso_animal = int(input("Ingrse el peso del Animal :    "))

            if peso_animal > 25:
                paciente_grande += 1
            else:
                paciente_grande += 1
        except ValueError:
            print("Ingrese uan opcion valida ")

print()
print(f"La clínica ha registrado {paciente_grande} pacientes grandes y {paciente_pequeño} pacientes pequeños. ¡Bienvenidos!")