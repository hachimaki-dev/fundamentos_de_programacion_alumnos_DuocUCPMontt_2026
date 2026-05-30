# Nombre de usuario para una app bancaria
# Un banco digital pide al usuario crear un nombre de usuario. Las reglas son:
# Mínimo 6 caracteres
# Sin espacios
# Si no cumple, muestra:
# "Nombre inválido. Debe tener al menos 6 caracteres y no contener espacios."
# Ejemplos válidos: juanp23, mariatorres, cliente99 Ejemplos inválidos: juan, maria torres, ok
# Cuando sea válido:
# "Usuario creado: juanp23"

# Creo lista vacia
lista_contraseñas = {}
# Que repita hasta que :
while True:
    # El try / except pongo dentro un str que es un string y lo pongo como input
    try:
        nombre_usuario = str(input("Ingrese el nombre de usuario \n"))
        # Si nombre_usuario tiene mas o igual a 6 caracteres y hay espacios " " en nombre_usuario entonces :
        if len(nombre_usuario) >=6 and " " not in nombre_usuario:
            print(f"Usuario creado : {nombre_usuario}")
            # Le digo que en el diccionario añada un espacio llamado "contraseña" y que sea igual a input añadido
            lista_contraseñas["contraseña"] = nombre_usuario
            # imprimo para verificar que todo esta correcto
            print(lista_contraseñas)
            # termino el while
            break
        else:
            print("Nombre de usuario invalido , debe tener 6 caracteres minimo y sin espacios")
    # Excepto si todos los Error que haya que lo guarde como una variable para despues mostrarlo en pantalla
    except Exception as error_de_escritura:
        print(f"Ocurrio un error inesperado {error_de_escritura}")
