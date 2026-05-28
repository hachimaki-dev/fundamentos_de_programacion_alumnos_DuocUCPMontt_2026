correcto = False
while correcto == False:
    
    nombre_de_usuario = input("Ingrese un nombre de usuario: ")
    tamaño_nombre = nombre_de_usuario.__len__()
    
    if tamaño_nombre < 6:
        print("ingrese un nombre de al menos 6 caracteres y sin ningun espacio 1")
        continue
    elif tamaño_nombre >= 6:
        for caracteres in nombre_de_usuario:
            if caracteres == " ":
                print("ingrese un nombre de al menos 6 caracteres y sin ningun espacio")
                break
        print("Checkpoint")
        correcto = True

        

print(f"Usuario creado: {nombre_de_usuario}")

