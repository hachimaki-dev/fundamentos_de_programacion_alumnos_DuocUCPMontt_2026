
print("===== NUMERO SECRETO =====")

numero_secreto = 7

print("Hola querido jugador, el número secreto es un número entero entre 1 y 10")
jugar_o_no_jugar = input("¿Quieres jugar? (si/no): ")

if jugar_o_no_jugar == "si" or jugar_o_no_jugar == "SI" or jugar_o_no_jugar == "Si":
    print("Excelente, comencemos >:3")
    
    # Este bucle se repite siempre que el numero sea incorrecto
    while True:
        numero_usuario = int(input("ingrese su numero: "))
        
        if numero_usuario == numero_secreto:
            print("¡GANASTE! Ese era el número secreto :3")
            break # Aquí se sale porque ya adivinaste
        
        else:
            print("Numero incorrecto, intente de nuevo >:C")
            
            
            

elif jugar_o_no_jugar == "no" or jugar_o_no_jugar == "No" or jugar_o_no_jugar == "NO":
    print("No hay problema, cuidate mucho >:3")
    
