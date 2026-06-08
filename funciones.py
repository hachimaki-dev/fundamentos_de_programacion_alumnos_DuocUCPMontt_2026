#Funciones sin retorno

def saludar():
    print("Hola desde la función saludar")

saludar()


#Funciones con retorno

def calcular_daño(raza):
    if raza == "Enano":
        return 20
    elif raza == "Elfo":
        return 3
    else :
        return 10
    
resultado = calcular_daño("Enano")
print("El daño calculado es:", resultado)