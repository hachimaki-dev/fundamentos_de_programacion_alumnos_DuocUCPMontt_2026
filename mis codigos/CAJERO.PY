saldo = 50.000
PIN = 1234
maxima_cantidad_intentos = 3
intentos_realizados = 0

print("===== CAJERO AUTOMATICO =====")

acceso_clave_usuario = int(input("ingrese PIN:"))

while True:
    if acceso_clave_usuario == PIN:
        print(f"1. giro rapido por $10.000")
        print(f"2. giro rapido por $20.000")
        print(f"3. giro rapido por $30.000")
        print(f"4. giro rapido por $40.000")
        print(f"5. giro rapido por $50.000")
        print(f"6. giro por otro monto")
        eleccion_usuario = input("(1/2/3/4/5/6:)")
        
        if eleccion_usuario == "1":
            print(f"1. giro rapido por $10.000")
            break

        elif eleccion_usuario == "2":
            print(f"2. giro rapido por $20.000")
            break

        elif eleccion_usuario == "3":
            print(f"3. giro rapido por $30.000")
            break

        elif eleccion_usuario == "4":
            print(f"4. giro rapido por $40.000")
            break

        elif eleccion_usuario == "5":
            print(f"5. giro rapido por $50.000")
            break

        elif eleccion_usuario == "6":
            otro_monto = int(input("ingrese otro monto:"))
            print(f"giro por ${otro_monto}")
            break
            
    else:
        print("PIN incorrecto intente de nuevo")
        break