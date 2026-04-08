saldo = 50000 

while True:
   print(" menú:")
   print("1- saldo")
   print("2- girar dinero")
   print("3- inversion")
   print("4- salir")

   opcion = input("selecione una opcion:") 

   if opcion == "1":
            print(f"saldo actual:{saldo}")
                  
   elif opcion == "2":
         monto = int(input("ingrese monto"))
         saldo= saldo - monto 
         print(f"nuevo saldo: {saldo}") 
                  
                        
   elif opcion == "3":
         monto = int(input("ingrese monto"))
         saldo = saldo + monto 
         print("hacer inversion")
            
                           
   elif opcion == "4":
         print("salir")
         break
   else:

            print("opcion invalida") 