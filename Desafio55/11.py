c_intentos_fallios = 0
clave_puesta = "Admin123"
clave_correcta = "secreto"
if clave_puesta == clave_correcta:
    print("Acceso aprobado")
else:
    c_intentos_fallios += 1
    print(f"Intentos fallidos: {c_intentos_fallios}")