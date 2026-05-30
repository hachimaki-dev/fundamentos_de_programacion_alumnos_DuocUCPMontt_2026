
while True:
    codigo_del_producto = input("Ingrese el codigo del Producto :   ").upper()
    if len(codigo_del_producto) < 6 or " " in codigo_del_producto:
        print("Error el codigo debe de contener al menos 6 carecteres o no tener espacios ")
        continue
    else:
        print(f"Producto Registrado Con Codigo : {codigo_del_producto}")
        break
