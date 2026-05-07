codigos = [200, 404, 500, 200, 500]
intentos = 1

for codigo in codigos:
    
    if codigo == 200:
        print(f"OK: {codigo} encontrado")
        
    elif codigo == 404:
        print(f"No encontrado {codigo}")
        
    elif codigo == 500:
        intentos -= 1
        print("Reintentando")
        
  
    if intentos <= 0:
        print("Servidor caido")
        break

        

    
    