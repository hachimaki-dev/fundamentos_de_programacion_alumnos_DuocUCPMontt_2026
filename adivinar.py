#declaro mis variables 
n_secreto = 7 
o_elegida = 0
#bucle para escoger un numero al azar mientras no acerte no sale del bucle
while n_secreto != o_elegida :
   o_elegida = int(input("elija un numero"))
   #Si o_elegida es diferente de n_secreto entonces imprime que me equivoque o en el caso contrario acerte con la respuesta
   if o_elegida != n_secreto:
    print("te equivocaste")
   #entonces colocamos un break para que termine el programa si no , entrara en el bucle infinitamente , consumiendo recursos innecesariamente 
   else:
    print("Es correcto") 
   break