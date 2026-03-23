print("BIENVENIDOS A MCDONALS, ESCOJA SU MENÚ")

while True:
    print(input("1. Combo MCpollo por solo $18.990"))
    print(input("2. Combo MCflurry super nova por solo $8.990"))
    print(input("3. Big mac por solo $7.990"))
    print(input("4. Combo kfc + mcdonals por $30.990"))
    print(input("5. Salir"))
    
    opcion = int(input("elija su menú :"))
    
    if opcion == 1:
        print("escojiste combo MCpollo por $18.990")
    if opcion == 2:
        print("escojiste Combo mcflurry super nova por $8.990")
    if opcion == 3:
        print("escojiste Big mac por $7.990")
    if opcion == 4:
        print("escojiste Combo KFC + MCdonals por $30.990")
    if opcion == 5:
        break 
    
    