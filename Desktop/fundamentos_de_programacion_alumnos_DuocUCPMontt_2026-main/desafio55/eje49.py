#prende a meterte dentro de un diccionario que tiene otro diccionario adentro (datos anidados).

#Datos Iniciales: Los permisos del usuario son: `admin = {'rol': 'dev', 'permisos': {'S3': True, 'EC2': False}}`.

#Reglas de Negocio: El usuario quiere prender un servidor 'EC2'. Tienes que revisar en sus permisos si tiene la autorización (True o False) para hacerlo.

#Restricciones: Como es un diccionario dentro de otro, tienes que encadenar los corchetes (ej. `diccionario['llave_padre']['llave_hijo']`) dentro de tu `if`. Si tiene permiso imprime 'Creando instancia', sino imprime 'Acceso Denegado'.

admin = {"rol": "dev", "permisos": {"S3": True, "EC2": False}}
if admin["permisos"] ["EC2"]:
    print("creando instancia")
else:
    print("acceso denegado")
    