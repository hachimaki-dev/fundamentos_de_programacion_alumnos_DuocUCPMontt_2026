total_dia = 0
pasajes = 0

print("-----Bienvenido a la Boleteria-------")

destinos = ["Puerto Varas" , "Frutillar" , "Osorno"]
precio_viaje = [3000,5000,7000]


while True:
    try:
        destino_elegido = int(input(f"Que destino desea Elegir:\n1.{destinos[0]}\n2.{destinos[1]}\n3.{destinos[2]}\ningrese su destino: "))
        if destino_elegido == 1:
            print(f"has seleccionado {destinos[0]} y su precio normal es ${precio_viaje[0]} y de ida y vuelta serian ${precio_viaje[0]*2}")
            
            tipo_de_viaje = int(input("¿Desea ir solo ida o ida y vuelta?\n1.Ida\n2.Ida y Vuelta\nopcion:  "))
            if tipo_de_viaje == 1:
                print(f"Usted a elegido ir de ida lo cual equivale a {precio_viaje[0]}")
            elif tipo_de_viaje == 2:
                print(f"Usted a elegido ir de ida y vuelta lo cual equivale a ${precio_viaje[0]*2}")
            else:
                print("opcion no valida")
        elif destino_elegido == 2:
            print(f"has seleccionado {destinos[1]} y su precio normal es ${precio_viaje[1]} y de ida y vuelta serian ${precio_viaje[1]*2}")
             
            tipo_de_viaje = int(input("¿Desea ir solo ida o ida y vuelta?\n1.Ida\n2.Ida y Vuelta\nopcion:   "))
            if tipo_de_viaje == 1:
                print(f"Usted a elegido ir de ida lo cual equivale a ${precio_viaje[1]} ")
            elif tipo_de_viaje ==2:
                print(f"Usted a elegido ir de ida y vuelta lo cual equivale a ${precio_viaje[1]*2}") 
            else:
                print("opcion no valida")            
        elif destino_elegido == 3:
            print(f"has seleccionado {destinos[2]} y su precio normal es ${precio_viaje[2]} y de ida y vuelta serian ${precio_viaje[2]*2}")
            
            tipo_de_viaje = int(input("¿Desea ir solo ida o ida y vuelta?\n1.Ida\n2.Ida y Vuelta\nopcion:  "))
            if tipo_de_viaje == 1:
                print(f"Usted a elegido ir de ida lo cual equivale a ${precio_viaje[2]} ")
            elif tipo_de_viaje ==2:
                print(f"Usted a elegido ir de ida y vuelta lo cual equivale a ${precio_viaje[2]*2}")
            else:
                print("opcion no valida")
            
        else:
            print("Ingrese un destino valido ")
    except ValueError:
        print("Ingrese un destino valido") 



        #Aun no Terminada 
