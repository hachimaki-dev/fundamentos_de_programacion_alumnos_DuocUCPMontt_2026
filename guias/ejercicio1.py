
while True:
    try:
        numero_usuario = int(input("ingresa un numero :"))
        
        break
    except ValueError:
        print("Error: eso no es un numero entero")
        
print(f"numero valido {numero_usuario}")
   