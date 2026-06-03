Voluntarios = []

while True:
    try:
        registrar_voluntarios = int(input("Ingrese la Cantidad de Voluntarios a Registrar :      "))
        if registrar_voluntarios <= 0:
            print("Ingrese un numero entero positivo ")
        else:
            break
    except ValueError:
        print("Ingrese una opcion valida ")


for i in range(registrar_voluntarios):

    while True:

        nombre_clave = input("Ingrese su nombre Clave :  ")
        if len(nombre_clave) < 4 or  " " in nombre_clave:
            print("Ingrese un Nombre con minimo 4 caracteres y sin espacios")
        else:
            break

    while True:
        try:
            horas_trabajo = int(input("Ingrese Las horas que puede Trabajar por semana :      "))
            if horas_trabajo <= 0:
                print("Ingrese un numero entero positivo")
            elif horas_trabajo > 20:
                titulo = "Voluntario Dedicado"
                break
            else:
                titulo = "Voluntario Casual"
                break
        except ValueError:
            print("ingrese una opcion valida")
        
    
    datos_clave = {"nombre" : nombre_clave , "Horas de Trabajo" : horas_trabajo , "Titulo" : titulo}
    Voluntarios.append(datos_clave)


print()
print("==== Registro Voluntarios ====")

for v in Voluntarios:

    print(f"Nombre : {v["nombre"]} | Horas de Trabajo : {v["Horas de Trabajo"]} | Titulo : {v["Titulo"]}")