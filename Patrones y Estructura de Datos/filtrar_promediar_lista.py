miembros = []
suma_tiempo = 0

while True:
    try:
        registrar_miembros = int(input("Ingrese cuantos Miembros se van a Registrar :   "))
        if registrar_miembros <= 0:
            print("Ingrese un nuemro entero positivo")
        else:
            break
    except ValueError :
        print("Ingrese una respuesta valida")

for i in range(registrar_miembros):
    while True:
        nombre_registrado = input("Ingrese su Nombre :  ").lower()
        if len(nombre_registrado) <= 0 :
            print("Ingrese una respuesta valida")
        else:
            break
    
    while True:
        try:
            tiempo_inscrito = int(input("Ingrese Cuantos meses lleva Registrado :   "))
            if tiempo_inscrito <= 0:
                print("Ingrese un numero entero positivo ")
            elif tiempo_inscrito > 6:
                suma_tiempo += tiempo_inscrito
                rango = "Miembro Frecuente"
                break
            else:
                rango = "Miembro regular"
                suma_tiempo += tiempo_inscrito
                break
        except ValueError:
            print("Ingrese una opcion valida ")

    miembros.append({"nombre" : nombre_registrado , "Tiempo Inscrito" : tiempo_inscrito , "Rango" : rango})


promedio = suma_tiempo / registrar_miembros

print()
print("======= Miembros Inscritos ==========")

for m in miembros:

    print(f"Nombre : {m["nombre"]} | Tiempo Inscrito : {m["Tiempo Inscrito"]} | Rango : {m["Rango"]}")


print(f"El Promedio de meses De todos los miembros  es {promedio:.2f}")