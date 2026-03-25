# diagrama: https://drive.google.com/file/d/108REciLYbb94HizhGOobPLY8hQJwTb9I/view?usp=drive_link

print("\n***********BIENVENIDO*************")

precio_producto = 0
tipo_producto = ""

while precio_producto == 0:
    print("\nSELECCIONE EL PRODUCTO: ")
    print("1. Agua ($1000)")
    print("2. Bebida ($1500)")
    print("3. Jugo ($1200)")

    seleccion = input("\nSeleccione 1, 2 o 3 (o 9 para salir): ")

    if seleccion == "9" :
        break

    if seleccion == "1":
        tipo_producto = "Agua"
        precio_producto = 1000 
   
    if seleccion == "2":
        tipo_producto = "Bebida"
        precio_producto = 1500 

    if seleccion == "3":
        tipo_producto = "Jugo"
        precio_producto = 1200 
    
    if seleccion != "1" and seleccion != "2" and seleccion != "3": 
        print("\nXXXXXXXXXXXXXXXXXXXXXXXXXX")
        print("ERROR: Seleccion no valida")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXX")

if precio_producto > 0 :
    print("\n**********PAGO**************")
    print(f"Producto seleccionado: {tipo_producto}")
    print(f"Monto a pagar: ${precio_producto}")
else :
    print("\n¡Vuelva pronto!\n")