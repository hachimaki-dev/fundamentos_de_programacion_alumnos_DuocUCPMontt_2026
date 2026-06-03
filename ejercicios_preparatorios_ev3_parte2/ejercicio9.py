while True:
    try:
        cantidad_voluntarios = int(input("¿Cuantos voluntarios desea registrar?: "))
        if cantidad_voluntarios > 0:
            break
        print("Solo se permiten numeros positivos.")
    except ValueError:
        print("Dato invalido: Ingrese un numero positivo")

voluntarios = []
voluntario_dedicado = 0
voluntario_casual = 0

for i in range(cantidad_voluntarios):
    print(f"Voluntario numero {i+1}")
    while True:
        nombre_voluntario = input("Ingrese el nombre del voluntario: ").strip()
        if len(nombre_voluntario) >= 4 and " " not in nombre_voluntario and nombre_voluntario.isalnum():
            break
        print("Código inválido. Mínimo 4 caracteres, sin espacios y alfanumérico.")
    
    while True:
        try:
            horas = int(input("Ingrese las horas que puede trabajar por semana: "))
            if horas > 0:
                break
            print("Solo se permiten numeros positivos.")
        except ValueError:
            print("Dato invalido: Ingrese un numero positivo")

    
    if horas > 20:
        print("Voluntario Dedicado")
        voluntario_dedicado += 1
    else:
        print("Voluntario Casual")
        voluntario_casual += 1
    
    voluntario = {"nombre": nombre_voluntario, "horas": horas}
    voluntarios.append(voluntario)


print("----- RESUMEN VOLUNTARIOS -----")
for voluntario in voluntarios:
    print(f"Nombre: {voluntario["nombre"]} | Horas: {voluntario["horas"]}")       