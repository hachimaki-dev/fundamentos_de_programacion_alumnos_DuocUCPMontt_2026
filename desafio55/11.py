intentos_falidos = 0
clave = "admin123"
introducir_contra = input("introdusca contraseña")
if introducir_contra == clave:
    print("entraste")
else:
    intentos_falidos += 1
    print("intentelo de nuevo")
    print("intentos fallidos")
    print(intentos_falidos)