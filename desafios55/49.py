admin = {'rol': 'dev', 'permisos': {'53': True, 'EC2': False}}
if admin['permisos']['EC2']:
    print("creando instancia")
else:
    print("acceso denegado")
    