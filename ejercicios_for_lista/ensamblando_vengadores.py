vengadores = []

print("#####"*15)
print("E n s a m  b l a n d o  a  l o s    V e n g a d o r e s")
print("#####"*15)


while True:
    print("M  E  N  U:\n1. Agregar Avenger\n2. Mostrar Base y modificar\n3. Salir")
    opcion = input("Que Opcion Desea Realizar (1/2/3 o 'sacrificar'): ")
    if opcion == "1":
        nombre_heroe = input("Que nombre tiene el Heroe que desea Agregar:   ")
        vengadores.append(nombre_heroe)
    elif opcion == "2":
        for i in range(len(vengadores)):
            print(f"{i} - {vengadores[i]}")
            vengadores[i] = vengadores[i].upper()
    elif opcion.lower() == "sacrificar":
            if len(vengadores) > 0:
                vengadores.pop()
            else:
                print("No hay vengadores para sacrificar")
    elif opcion == "3":
    
        print(" S a l i o  d e l   S i s t e m a")
        break
    else:
        print(" S a l i o  d e l   S i s t e m a")
        break
