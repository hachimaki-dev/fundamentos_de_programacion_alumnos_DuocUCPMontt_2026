vida_jefe = 1000

print("*****************************")
print("Bienvenido a la pelia final")
print("*****************************")

print (f"la vida del jefe es de {vida_jefe}")
# el whilr sirve como contador de la vida del jefe
while vida_jefe > 0:
   
     daño = int(input("cuanto es el daño que le quieres hacer al jefe: "))



     if daño < 0: 
        print("fallaste el ataque")
    
     else:
        vida_jefe -= daño
        vida_actual = max(0,vida_jefe)
        print(f"buen golpe le queda {vida_actual}")

print("********************")
print("¡JEFE DERROTADO!")
print("********************")

         
