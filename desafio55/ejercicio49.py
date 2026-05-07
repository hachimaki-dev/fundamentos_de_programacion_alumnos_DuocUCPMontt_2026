admin = {'rol': 'dev', 'permisos': {'S3': True, 'EC2': False}}
print("El usuario quiere prender un servidor EC2")
if admin['permisos']["EC2"] ==  True:
    print("Acceso permitido")
else:
    print("Acceso denegado")