Tijera = 1
Piedra = 2
Papel = 3
Salir = 0


Marcador_jugador_1 = 0
Marcador_jugador_2 = 0


while True :
    print("1.Tijera")
    print("2.Piedra")
    print("3.Papel")
    print("0.Salir")
    opcion_jugador_1 = int(input("Tomás elija su opcion"))
    opcion_jugador_2 = int(input("Gabriel,elija su opcion"))
   
   
   
    while opcion_jugador_1 == 1 and opcion_jugador_2 == 1 :

        print("Tomás lanzo Tijera")
        print("Gabriel lanzo Tijera")
        print("Empate,Ninguno gana puntos,Vuelva a intentarlo")
        break
   
    while opcion_jugador_1 == 2 and opcion_jugador_2 == 2 :
        
        print("Tomás lanzo piedra")
        print("Gabriel lanzo piedra")
        print("Empate,Ninguno gana puntos,Vuelva a intentarlo")
        break
   
    while opcion_jugador_1 == 3 and opcion_jugador_2 == 3 :

        print("Tomás lanzo Papel")
        print("Gabriel lanzo Papel")
        print("Empate,Ninguno gana puntos,Vuelva a intentarlo")
        break
   
    if opcion_jugador_1 == 1 and opcion_jugador_2 == 3 :
        print("Tomás lanzo Tijera")
        print("Gabriel lanzo Papel")
        print("*PUNTO PARA TOMÁS*")
        
        Marcador_jugador_1 = Marcador_jugador_1 + 1
        
        print("Marcador:")
        print("Tomás:", Marcador_jugador_1)
        print("Gabriel:", Marcador_jugador_2)
   
   
    if opcion_jugador_1 == 2 and opcion_jugador_2 == 1 :

        print("Tomás lanzo Piedra")
        print("Gabriel lanzo Tijera")
        print("*PUNTO PARA TOMÁS*")
       
        Marcador_jugador_1 = Marcador_jugador_1 + 1
       
        print("Marcador:")
        print("Tomás:", Marcador_jugador_1)
        print("Gabriel:", Marcador_jugador_2)
   
    if opcion_jugador_1 == 3 and opcion_jugador_2 == 2 :
        
        print("Tomás lanzo Papel")
        print("Gabriel lanzo piedra")
        print("*PUNTO PARA TOMÁS*")
       
        Marcador_jugador_1 = Marcador_jugador_1 + 1 
       
        print("Marcador:")
        print("Tomás:", Marcador_jugador_1)
        print("Gabriel:" , Marcador_jugador_2)
    
    if opcion_jugador_2 == 1 and opcion_jugador_1 == 3 :
       
        print("Tomás lanzo Papel")
        print("Gabriel lanzo Tijera")
        print("*PUNTO PARA GABRIEL*")
        
        Marcador_jugador_2 = Marcador_jugador_2 + 1
        
        print("Marcador:")
        print("Tomás:", Marcador_jugador_1)
        print("Gabriel:", Marcador_jugador_2)
    
    if opcion_jugador_2 == 2 and opcion_jugador_1 == 1 :
       
        print("Tomás lanzo Tijera")
        print("Gabriel lanzo Piedra")
        print("*PUNTO PARA GABRIEL*")
        
        Marcador_jugador_2 = Marcador_jugador_2 + 1

        print("Marcador:")
        print("Tomás:", Marcador_jugador_1)
        print("Gabriel:", Marcador_jugador_2)

    if opcion_jugador_2 == 3 and opcion_jugador_1 == 2 :
        
        print("Tomás lanzo Piedra")
        print("Gabriel lanzo Papel")
        print("*PUNTO PARA GABRIEL*")

        Marcador_jugador_2 = Marcador_jugador_2 + 1

        print("Marcador:")
        print("Tomás:", Marcador_jugador_1)
        print("Gabriel:", Marcador_jugador_2)

    if Marcador_jugador_1 == 3 :
        print("****GANO TOMÁS****")
       
        break
  
    if Marcador_jugador_2 == 3 :
        print("****GANO GABRIEL****")
        
        break
    
    while opcion_jugador_1 >= 4 :
        
        print("Porfavor Tomás introduzca un numero mostrado para iniciar el versus :)")

        
        break
    
    while opcion_jugador_2 >= 4 :

        print("Porfavor Gabriel introduzca un numero mostrado para poder iniciar el versus :)")

        break
    
    if opcion_jugador_1 == 0 :
        print("Uno de los jugadores salio del programa")
        break

    if opcion_jugador_2 == 0 :
        print("Uno de los jugadores salio del programa")
        break
        
       

    
        


        
        
        
        
print("***--FIN DE PROGRAMA--***")


        






    

    


    
    

        


        

    



     
     


        
     
     
    


 



    

    
        


    
    
    
    

   





