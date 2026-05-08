admin = {
    "rol": "dev",
    "permisos": {
        "s3": True,
        "EC2": False
        }
}

if admin ["permisos"]["EC2"]:
    print("Creando instancia")
else:
    print("Acesso concedido")