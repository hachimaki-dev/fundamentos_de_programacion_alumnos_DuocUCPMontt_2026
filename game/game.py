print("bienvenido")
print("!!!PRIMERO EL NUMERO Y DESPUES LA LETRA!!!, PISTA 0A ES MINA!!")
contador = 0
minas = ["0A","2B","3B", "4E", "1D", "3D", "0E", "1E"] #MINAS
espacios = ["0B", "0C", "0D", 
           "1A", "1C", "1D", 
           "2A", "2B", "2C", "2E",
           "3A", "3C", "3E",
           "4A", "4C", "4D" ,"5f",3,3,3,3,3,3,3,3,3,3,3,3,3,]

#0
a0a = "X"
a0b = "X"
a0c = "X"
a0d = "X"
a0e = "X"
#1
a1a = "X"
a1b = "X"
a1c = "X"
a1d = "X"
a1e = "X"
#2
a2a = "X"
a2b = "X"
a2c = "X"
a2d = "X"
a2e = "X"
#3
a3a = "X"
a3b = "X"
a3c = "X"
a3d = "X"
a3e = "X"
#4
a4a = "X"
a4b = "X"
a4c = "X"
a4d = "X"
a4e = "X"

for contador in range(len(espacios)):
    print(" A B C D E")
    print(" -------------------")
    print("0 |", a0a, "|", a0b, "|", a0c, "|", a0d, "|", a0e, "|")
    print("1 |", a1a, "|", a1b, "|", a1c, "|", a1d, "|", a1e, "|")
    print("2 |", a2a, "|", a2b, "|", a2c, "|", a2d, "|", a2e, "|")
    print("3 |", a3a, "|", a3b, "|", a3c, "|", a3d, "|", a3e, "|")
    print("4 |", a4a, "|", a4b, "|", a4c, "|", a4d, "|", a4e, "|")

    respuesta = input("ingrese sitio a cavar: ").upper()
    
    if respuesta in minas:
        print("BOOOOOOMMMMMMM")
        print("fin")
        break
    
    elif respuesta in espacios:
        print("no hay mina")
        if respuesta == "0B":
            a0b = 1
        elif respuesta == "0C":
            a0c = 1
        elif respuesta == "0D":
            a0d = 3
            
        #1
        elif respuesta == "1A":
            a1a = 2
        elif respuesta == "1C":
            a1c = 2
            
        #2
        elif respuesta == "2A":
            a2a = 2
        elif respuesta == "2C":
            a2c = 4
        elif respuesta == "2E":
            a2e = 2
            
        #3
        elif respuesta == "3A":
            a3a = 2
        elif respuesta == "3C":
            a3c = 3
        elif respuesta == "3E":
            a3e = 1
            
        #4
        elif respuesta == "4A":
            a4a = 1
        elif respuesta == "4B":
            a4b = 1
        elif respuesta == "4C":
            a4c = 2
        elif respuesta == "4D":
            a4d = 2
    if espacios == 0:
        print("ganaste")
        break