# Ejercicio 11: Clave Única Básico

print("===============================")
print("Bienvenido al sistema de acceso")
print("===============================")

intentos_fallidos = 0

clave_escrita = "Admin123"
clave_correcta = "secreto"

if clave_escrita == clave_correcta:
    print("Acceso permitido")
else:
    intentos_fallidos = intentos_fallidos + 1
    print("Intentos fallidos:", intentos_fallidos)