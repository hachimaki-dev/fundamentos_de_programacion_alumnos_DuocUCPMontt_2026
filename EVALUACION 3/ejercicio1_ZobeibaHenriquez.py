#Definimos las categorias
senior = []
junior = []

#Solicitamos la cantidad de ingenieros
while True:
    try:
        cantidad_ing = int(input("¿Cuántos ingenieros deseas ingresar? "))
        if cantidad_ing <= 0:
            print("Error: La cantidad debe ser mayor a 0.")
        else:
            break
    except ValueError:
        print("Error: Ingrse un cantidad válidad, debe ser entero positivo.")

#Ahora vamos a recorrer la cantidad de ingenieros, para solicitarle cada uno un alias y nivel de exp
for i in range(cantidad_ing):
    
#Solicitamos el alias :D
    while True:
        alias = input(f"\nAlias del ingeniero {i + 1}: ").strip()
        if len(alias) >= 6 and " " not in alias and alias.isalnum():
                break
        else:
            print("Error: el alias debe contener mínimo 6 caracteres, sin espacios ni caracteres especiales.")

#Solicitamos nivel tecnico
    while True:
        try:
            nivel_tecnico = int(input(f"\nNivel técnico del ingeniero {alias}: "))
            if nivel_tecnico <= 0:
                print("Error: El nivel técnico debe ser mayor a 0.")
            else:
                break
        except ValueError:
            print("Error de validación: Ingresa un número entero positivo para el nivel técnico.")

#Clasificamos a los ingenieros según su nivel tecnico    
    if nivel_tecnico > 45:
        senior.append({alias : nivel_tecnico})
        print(f"Ingeniero {alias} registrado como Senior (nivel {nivel_tecnico})")
    else:
        junior.append({alias : nivel_tecnico})
        print(f"Ingeniero {alias} registrado como Junior (nivel {nivel_tecnico})")

#Resumen      
print("\n----------------------------------------------------------------------------------------------------------------------------------------------")
print(f"Ingeniero Senior= {senior}")
print(f"Ingeniero Junior = {junior}")
print(f"¡El instituto cuenta con {len(senior)} Ingeniero(s)Senior y {len(junior)} Ingeniero(s) Junior! ¡Registro completado satisfactoriamente!")
print("------------------------------------------------------------------------------------------------------------------------------------------------")