#Aprende a meterte dentro de un diccionario que tiene otro diccionario adentro (datos anidados).

admin = {
    'rol': 'dev',
    'permisos': {
        'S3': True,
        'EC2': False
    }
}

#Reglas de Negocio: El usuario quiere prender un servidor 'EC2'. Tienes que revisar en sus permisos si tiene la autorización (True o False) para hacerlo.

#Restricciones: Como es un diccionario dentro de otro, tienes que encadenar los corchetes (ej. `diccionario['llave_padre']['llave_hijo']`) dentro de tu `if`. Si tiene permiso imprime 'Creando instancia', sino imprime 'Acceso Denegado'.


if  admin['permisos']["EC2"]:
    print("Creado instancia")
else:
    print("Acceso Denegado")