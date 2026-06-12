while True:
    
    try:
        edad = int(input("ingrese su edad para continuar con la compra:"))
        if edad >= 18:
            break
        else:
            print("Error: su edad es insuficiente")
    except ValueError:
        print("Error: su edad es insuficiente\nIntente denuevo:")
    
print("usted tiene", edad ,"años, esta autorizado para comprar")
    