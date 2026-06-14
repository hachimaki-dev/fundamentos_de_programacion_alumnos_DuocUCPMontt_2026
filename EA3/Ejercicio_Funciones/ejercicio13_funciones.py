def validar_precio(precio):
    if isinstance(precio,(int, float)):
        if precio >= 1000 and precio <=50000:
            return True
        else:
            return False
    else: 
        return False
def solicitar_precio_valido():
    while True:
        entrada = input("Ingrese el precio: ")
        try:
            precio_numerico = float(entrada)
            if validar_precio(precio_numerico):
                return precio_numerico
            else:
                print("Error: El precio debe estar entre 1000 y 50000")
        except ValueError:
            print("Error: Debe ingresar un numero valido")