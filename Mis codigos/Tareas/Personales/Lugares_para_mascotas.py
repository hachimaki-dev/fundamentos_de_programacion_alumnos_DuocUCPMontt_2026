print("--LUGARES PARA IR CON TUS MASCOTAS--")

while True:
    
    tipo_de_espacio = input("BIENVENIDO. ¿QUE TIPO DE ESPACIO TE GUSTARIA IR CON TU MASCOTA EL DIA DE HOY?\n1).Espacios abiertos\n2).Espacios cerrados\n")
    
    while tipo_de_espacio != "1" and tipo_de_espacio != "2":
        tipo_de_espacio = input("\nSeleccione una opcion vàlida. Recuerde colocar el nùmero de la opciòn deseada\n")

    if tipo_de_espacio == "1":
        print("--PERFECTO. ESTOS SON TODOS LOS ESPACIOS ABIERTOS EN LOS QUE PUEDES IR CON TUS MASCOTAS--\n")
        print("1).Parque Costanera Puerto Montt\n2).Parque Municipal la Paloma\n3).Parque Luis Abel\n4).Parque Alerce Andino\n5).Divertican (Parque Canino)\n")
        espacio_cerrado = input("¿DÒNDE DESEA IR CON SU MASCOTA?\n")
        if espacio_cerrado == "1":
            print("Google Maps: 📍 -41.4739146, -72.9437722")
            break

        elif espacio_cerrado == "2":
            print("Google Maps: 📍 -41.4517884, -72.9081914")
            break

        elif espacio_cerrado == "3":
            print("Google Maps: 📍 -41.4636087, -72.9028873")
            break

        elif espacio_cerrado == "4":
            print("Google Maps: 📍 -41.5045, -72.5806")
            break

        elif espacio_cerrado == "5":
            print("Google Maps: 📍 -41.438, -72.853")
            break

        while espacio_cerrado != "1" and espacio_cerrado != "2" and espacio_cerrado != "3" and espacio_cerrado != "4" and espacio_cerrado != "5":
            espacio_cerrado = input("\nRespuesta no vàlida. Recuerde colocar el nùmero de la opciòn deseada\n")

    
    elif tipo_de_espacio == "2":
        print("--PERFECTO. SELECCIONE EL TIPO--")
        print("1).Cafeterìas / Comidas\n2).Tiendas Pet Friendly\n3).Servicios\n")
        tipo_de_espacio_cerrado = input("")
        if tipo_de_espacio_cerrado == "1":
            print("HA ELEGIDO CAFETERIAS / COMIDAS. A CONTINUACIÒN LES ENTREGARÈ LAS OPCIONES QUE TIENE DENTRO DE ESTA CATEGORIA")
            cafeterias_comidas = input("1).The kindom coffe\n")
            if cafeterias_comidas == "1":
                print("Google Maps: 📍 -41.4471942, -72.9282384")
                break

            while cafeterias_comidas != "1":
                cafeterias_comidas = input("\nRespuesta no vàlida. Recuerde colocar el nùmero de la opciòn deseada\n")

        elif tipo_de_espacio_cerrado == "2":
            print("HA ELEGIDO TIENDAS PET FRIENDLY. A CONTINUACIÒN LES ENTREGARÈ LAS OPCIONES QUE TIENE DENTRO DE ESTA CATEGORIA")
            pet_friendly = input("1).Mascota Manìa\n2).Para mi mascota\n")
           
            if pet_friendly == "1":
                print("Google Maps: 📍 -41.45065, -72.92081")
                break
            elif pet_friendly == "2":
                print("Google Maps: 📍 -41.4589682, -72.9046176")
                break
            while pet_friendly != "1" and pet_friendly != "2":
                pet_friendly = input("\nRespuesta no vàlida. Recuerde colocar el nùmero de la opciòn deseada\n")
            
        elif tipo_de_espacio_cerrado == "3":
            print("HA ELEGIDO SERVICIOS. A CONTINUACIÒN LES ENTREGARÈ LAS OPCIONES QUE TIENE DENTRO DE ESTA CATEGORIA")
            servicio = input("1).Taxi Mascota Puerto Montt\n2).Peluqueria canina Mundo Mascotas\n")
            
            if servicio == "1":
                print("Contacto:\n📞 +56 9 6213 6541\n💬 WhatsApp directo disponible\n📍 Atención 24/7")
                break

            elif servicio == "2":
                print("Contacto:\n📞 +56 9 8139 2037")
                break
            
            while servicio != "1" and servicio != "2":
                servicio = input("\nRespuesta no vàlida. Recuerde colocar el nùmero de la opciòn deseada\n")


        while tipo_de_espacio_cerrado != "1" and tipo_de_espacio_cerrado != "2" and tipo_de_espacio_cerrado != "3":
            tipo_de_espacio_cerrado = input("\nRespuesta no vàlida. Recuerde colocar el nùmero de la opciòn deseada\n")
        


