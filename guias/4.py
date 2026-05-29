while True :

    
    
    nombre_banco = input("ingrese su nombre: ")

    if " " in nombre_banco or (len(nombre_banco)) < 6 :
            
       print("Nombre invalido: no puede tener menos que 6 caracteres o contener espacios ")
       continue
    else:
        print(f"Usuario creado: {nombre_banco}")
        break
