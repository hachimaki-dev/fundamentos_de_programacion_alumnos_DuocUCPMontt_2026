admin = {
    'rol' : 'dev',
    'permisos' : {
        'S3' : True,
        'EC2' : False
    }
}

if admin['permisos']['EC2'] == True:
    print("Creando instancia")
elif admin['permisos']['EC2'] == False:
    print("Acceso denegado")