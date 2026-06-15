bichos=[]
#def bichos_capturados():
#Debes definir dos funciones separadas para el menú: una que muestre las opciones en pantalla (sin recibir ni retornar nada)
#Y otra que lea y retorne la opción elegida por el usuario (sin recibir nada, retornando el número validado).
#Ambas funciones deben invocarse en cada vuelta del ciclo.

def mostrar_menu():
    print("\n========== MENÚ PRINCIPAL ========== \n1. Agregar bicho \n2. Buscar bicho \n3. Eliminar bicho \n4. Actualizar estados \n5. Mostrar bichos \n6. Salir \n=====================================\n")
while True:
    opcion_usuario=int(input("Por favor ingresa el número de la opción que deseas elegir: "))
    if opcion_usuario==1:
        nombre_del_bicho=input("Por favor ingresa el nombre del bicho: ")
        tamano_del_bicho=int(input("Por favor ingresa el tamaño del bicho: "))
        peligrocidad_del_bicho=float(input("Por favor ingresa el nivel de peligrosidad del bicho (1.0-10.0): "))
        if peligrocidad_del_bicho>=7.0:
            peligroso=True
        else:
            peligroso=False
        bicho_capturado={"Especie": nombre_del_bicho, "Tamaño": tamano_del_bicho, "Peligrocidad": peligrocidad_del_bicho, "Peligroso": peligroso}
        bichos.append(bicho_capturado)
        print(f"¡Bicho {nombre_del_bicho} agregado exitosamente!")
    elif opcion_usuario==6:
        print("¡Gracias por usar el programa! ¡Hasta luego!")
        break
