avengers = []
programa = True
print ("""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣤⣴⣶⣶⣾⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣠⣴⣿⣿⣿⠿⠿⠛⣻⣿⣿⣿⣿⣿⣿⣿⣦⣄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣠⣾⣿⡿⠛⠉⠀⠀⠀⣰⣿⣿⣿⠟⣿⣿⣿⣿⢿⣿⣷⣦⠀⠀⠀⠀
⠀⠀⢠⣾⣿⡟⠁⠀⠀⠀⠀⠀⣰⣿⣿⣿⡟⠀⣿⣿⣿⣿⠀⠈⢻⣿⣷⡄⠀⠀
⠀⢠⣿⣿⠏⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⡟⠀⠀⣿⣿⣿⣿⠀⠀⠀⠹⣿⣿⡄⠀
⢀⣿⣿⠏⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⡿⠁⠀⠀⣿⣿⣿⣿⠀⠀⠀⠀⠸⣿⣿⡄
⣸⣿⡟⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⠃⠀⠀⠀⣿⣿⣿⣿⠀⠀⠀⠀⠀⢻⣿⣇
⣿⣿⡇⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⠇⠀⠀⠀⠀⣈⠻⣿⣿⠀⠀⠀⠀⠀⢸⣿⣿
⣿⣿⡇⠀⠀⠀⠀⢠⣿⣿⣿⣿⣯⣤⣤⣤⣤⣤⣿⣶⣌⠻⠀⠀⠀⠀⠀⢸⣿⣿
⢻⣿⣇⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡄⠀⠀⠀⠀⣸⣿⡟
⠘⣿⣿⡄⠀⢠⣿⣿⣿⣿⡿⠿⠿⠿⠿⠿⠿⢿⣿⣿⠟⢋⠀⠀⠀⠀⢠⣿⣿⠃
⠀⠹⣿⡿⢀⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀⠸⠋⣡⣴⣿⠀⠀⠀⣠⣿⣿⠏⠀
⠀⠀⠙⢁⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠚⠛⠛⠛⠀⢀⣴⣿⣿⠋⠀⠀
⠀⠀⢀⣾⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⣿⣿⠟⠁⠀⠀⠀
⠀⢀⣾⣿⣿⣿⣿⠏⣰⣿⣶⣦⣤⣤⣤⣤⣤⣤⣴⣶⣿⣿⡿⠛⠁⠀⠀⠀⠀⠀
⢀⣾⣿⣿⣿⣿⡟⠀⠈⠙⠛⠻⠿⠿⠿⠿⠿⠿⠟⠛⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀
""")

while programa == True:
    print("""
Seleccion una opción:
1) Agregar Avenger
2) Mostrar Base de datos
3) Salir          """)
    opcion = input("")
    if opcion == "1":
        print("INGRESE EL AVENGER")
        avengers.append((input("").upper()))
        
        print(f"debugeando {avengers}")
    elif opcion == "2":
        contador = 0
        for i in avengers:
            
            print(f"{contador} {i}")
    elif opcion == "Sacrificar":
        print (f"{avengers[-1]} Sacrificad@")
        avengers.pop()

    elif opcion == "3":
        break
        programa = False