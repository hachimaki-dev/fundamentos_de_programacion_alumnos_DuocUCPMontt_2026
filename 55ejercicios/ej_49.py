# Ejercicio 49: Verificación de Permisos (AWS)

print("====================================")
print("Verificación de permisos del usuario")
print("====================================")

admin = {'rol': 'dev', 'permisos': {'S3': True, 'EC2': False}}

if admin['permisos']['EC2'] == True:
    print("Creando instancia")
else:
    print("Acceso Denegado")