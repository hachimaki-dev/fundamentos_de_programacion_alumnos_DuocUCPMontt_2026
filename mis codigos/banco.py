while True:
    try:
        nombre_usuario = input("Crea un nombre de usuario (mínimo 6 caracteres y sin espacios): ")
        
        # Ponemos el contador aquí adentro para que se reinicie en cada intento
        total_de_caracteres = 0
        
        for i in nombre_usuario:
            if i == " ":
                raise ValueError  # Si encuentra un espacio, salta directo al except
            total_de_caracteres = total_de_caracteres + 1
        
        # Si termina el for y no llega a 6, también lanzamos error
        if total_de_caracteres < 6:
            raise ValueError
            
        # Si no hubo errores, felicidades, rompemos el while
        print(f"Usuario creado: {nombre_usuario}")
        break
        
    except ValueError:
        # Tu bloque except que atrapa los errores y vuelve a pedir el nombre
        print("Nombre inválido. Debe tener al menos 6 caracteres y no contener espacios.\n")