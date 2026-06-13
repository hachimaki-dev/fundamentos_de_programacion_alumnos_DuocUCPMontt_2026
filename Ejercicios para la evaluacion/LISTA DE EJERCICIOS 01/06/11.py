registrados_gym = []
meses_suma = 0
while True:
    try:
        cantidad_de_miembros = int(input("Cuantas personas quieres registrar en el gym? "))
        if cantidad_de_miembros <= 0:
            print("No puedes ingresar este numero, intenta con uno positivo entero.")
            continue
        else:
            break
    except ValueError:
        print("ERROR, no puede ingresar letras, debe ingresar numeros enteros.")

for miembro_gym in range(1, cantidad_de_miembros+1):
    nombre_miembro = input("Ingrese su nombre: ").strip()
    while True:
        try:
            meses_miembro = int(input("Ingrese la cantidad de meses que lleva en el gimnasio: "))
            if meses_miembro <= 0:
                print("ERROR, no puede ingresar 0 o menos que 0.")
                continue
            else:
                meses_suma += meses_miembro
                break
        except ValueError:
            print("ERROR, no puede ingresar letras.")
    if (nombre_miembro and meses_miembro) not in (registrados_gym):
        registrados_gym.append({"nombre": nombre_miembro, "meses": meses_miembro})
    else:
        print("Ya registrado.")

for i in registrados_gym:
    print(f"Nombre: {i["nombre"]} | Meses: {i["meses"]}")
for solo_6_meses in registrados_gym:
    if solo_6_meses["meses"] > 6:
        print(f"Los que estan registrados más de 6 meses: {solo_6_meses["nombre"]} con {solo_6_meses["meses"]} meses de registro.")
promedio = meses_suma/len(miembro_gym) if len(miembro_gym) > 0 else 0
print(f"El promedio de meses en total es de: {round(promedio,2)}")