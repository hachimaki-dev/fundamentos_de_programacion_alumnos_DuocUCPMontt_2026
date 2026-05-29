
    

while True:
    nombre_De_usuariobanco = input("ingrese su nombre de usuario")

    if " " in nombre_De_usuariobanco:
        print("no debe de tener espacios")
        continue


    if len(nombre_De_usuariobanco) <= 5:
        print("debe tener como minimo 6 digitos")
        continue
            
    print(f"Usuario creado: {nombre_De_usuariobanco}")
    break

   
    