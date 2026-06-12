while True:
    nombre = input("ingrese su nombre de usuario:")
    if len(nombre) >= 6 and " " not in nombre:
        break
    else:
        print("Error: su nombre debe tener mas de 5 letras y sin espacio")
        
print("usuario creado:", nombre)
   

