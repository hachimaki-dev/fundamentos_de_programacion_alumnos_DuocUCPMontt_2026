admin = {"rol" : "dev", "permisos": {"S3" : True, "ec2" : False}}
if admin["permisos"]["ec2"] == True:
    print("creando instancia")
else:
    print("acceso denegado")