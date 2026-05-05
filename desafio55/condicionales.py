
# Crea un contador `intentos_fallidos` en 0. Asume que escribiste la clave 'Admin123'.
 # La clave correcta es 'secreto'. Si la clave que escribiste es igual a la correcta, entraste. Si es diferente, suma 1 a tus intentos fallidos.
contraseña = "admin123"
contador = 0
guardar_contraseña = input("bienvenido al banco ,escriba tu contraseña: ") 
if guardar_contraseña == "admin123":
    print("contraseña correcta")
else:
    contador = contador + 1 
    print(f"intentos fallidos {contador}")






