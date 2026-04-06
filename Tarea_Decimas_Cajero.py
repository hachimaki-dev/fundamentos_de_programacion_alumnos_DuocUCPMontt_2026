saldo_usuario = 50000
PIN_usuario = 2008
intentos_contraseña = 3


while intentos_contraseña > 0 :
   
    ingresar_usuario = int(input("Ingrese su PIN:"))
      
         
    

    if ingresar_usuario == PIN_usuario :  
        

        
        print("MENU DE RETIRO")
   
    
        print("1. 1000")
     
        print("2. 5000")
     
        print("3. 10000")
     
        print("4. 20000")
     
        print("5. 50000")
     
        print("6. 100000")

        print("7. 200000")

        print("8.Salir")
     
        Eleccion_monto_usuario = int(input("Elija el monto que quiera retirar"))
     
        if Eleccion_monto_usuario == 0 :
           

           print("Monto invalido,Vuelva a intentarlo")

        if saldo_usuario < 0 :
        
           print("Fondos insuficientes")

        if Eleccion_monto_usuario == 8 :
           print("El usuario decidio salir del cajero")
           break

        
        if Eleccion_monto_usuario == 1 :
           monto = 1000
           
           
        
        elif Eleccion_monto_usuario == 2 :
       
           monto = 5000

        elif Eleccion_monto_usuario == 3 :
       
           monto = 10000
     
        elif Eleccion_monto_usuario == 4 :
          
          monto = 20000
        
        elif Eleccion_monto_usuario == 5 :
       
          monto = 50000

        elif Eleccion_monto_usuario == 6 :
           
           monto = 100000
        elif Eleccion_monto_usuario == 7 :
           
           monto = 200000
       
        else :
           monto = 0
           print("Opcion invalida")
        
        if monto > 0 :
           if saldo_usuario >= monto :
              saldo_usuario = saldo_usuario - monto
              print(f"Retiro exitoso,su nuevo saldo es {saldo_usuario}")

           else :
          
             print("Fondos insuficientes")
          
        break
     
    else : 
          
       
       intentos_contraseña = intentos_contraseña - 1
       print("Contraseña incorrecta") 
       print(f"te quedan {intentos_contraseña} intentos")

if intentos_contraseña == 0 :
          
      print("Tarjeta bloqueada por seguridad")
         
           
            
    
    
     
        
        
        

     
     
     
     
    
       
        


            

        



    

    

         







print("***FIN DEL PROGRAMA***")