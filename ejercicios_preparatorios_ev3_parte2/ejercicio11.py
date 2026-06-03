while True:
    try:
        cantidad_miembros = int(input("¿Cuantos miembros desea registrar?: "))
        if cantidad_miembros > 0:
            break
        print("Solo se permiten numeros positivos.")
    except ValueError:
        print("Dato invalido: Ingrese un numero positivo")

miembros = []

for i in range(cantidad_miembros):
    print(f" ---- Miembro numero {i+1} ----")
    while True:
        nombre_miembro = input("Ingrese el nombre del voluntario: ").strip()
        if len(nombre_miembro) > 0:
            break
        print("El nombre no puede estar vacio")

    while True:
        try:
            meses = int(input("Meses de membresia: "))
            if meses > 0:
                break
            print("Los meses deben ser mayor a 0")
        except ValueError:
            print("Dato invalido: Ingrese un numero positivo")

    miembro = {"nombre": nombre_miembro, "meses": meses}
    miembros.append(miembro)

suma_meses = 0
print("------ LISTA MIEMBROS ------")
for miembro in miembros:
    print(f"Nombre: {miembro["nombre"]} | Membresia: {miembro["meses"]} meses")
    suma_meses += miembro["meses"]

print("------ MIEMBROS FRECUENTES ------")
for miembro in miembros:
    if miembro["meses"] > 6:
        print(f"Nombre: {miembro["nombre"]} | Membresia: {miembro["meses"]} meses")

promedio_meses = suma_meses / cantidad_miembros
print(f"El promedio de meses de todos los miembros es de: {promedio_meses:.2f} meses")