admin = {"rol": "dev", "permisos": {
    "S3": True,
    "EC2": False
}}

servidor_pedido = "EC2"


if servidor_pedido in admin["permisos"]:
    if admin["permisos"][f"{servidor_pedido}"] == False:
        print("Acceso Denegado")
    else:
        print("Acceso garantizado")