admin = {'rol': 'dev', 'permisos': {'S3': True, 'EC2': False}}
if admin['permisos']['EC2'] == True:
    print("creando instancia")
else:
    print("acceso denegado")