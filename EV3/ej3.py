while True:
    try:
        cantidad =int(input("¿Cuantos atletas registrara?"))
        if cantidad > 0:
            break
        else:
            print("¡El numero debe ser mayor a 0!")
    except ValueError:
        print("---Error. Ingrese un numero---")

elites = 0
regulares = 0

for i in range(cantidad):
    print(f"\n --- atleta {i+1} ---")
    while True:
        codigo = (input("Ingrese el codigo: "))
        if len(codigo) >=5 and " " not in codigo and codigo:
            break
        print("Codigo invalido. Debe tener al menos 5 caracteres")
        
    while True:
        try:
            puntaje = int(input("Ingrese su puntaje: "))
            if puntaje > 0:
                break
            print("Ingrese un numero mayor a 0")
        except ValueError:
            print("Error ingrese un numero")
            
    if puntaje > 70:
        elites+=1
        print(" atletas elite")
    else:
        regulares+=1
        print(" atletas regular")
        
print(f"\n¡El centro cuenta con {elites} Atletas Élite y {regulares} Atletas Regulares! ¡Registro completado!")       