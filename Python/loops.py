#For 
#Bucle que se utiliza para iterar sobre una secuencia (como una lista , una tuplas o una cadena) o cualquier objeto iterable
# for variable in secuencia 
   # bloque de codigo a repetir 
   #instrucciones
frutas = ["manzana" , "banana" , "naranja"]
for fruta in frutas:
    print(fruta)

#While
#Bucle que se utiliza para repetir un bloque de codigo mientras una condicion sea verdadera.

# while condicion :
    # bloque de codigo a repetir
    # instrucciones
contador = 0 

while contador < 5 :
    print(contador)
    contador += 1

#Contro de bucles : para controlar el flujo de ejecucion dentro de los bucles :
# Break
contador = 0 
while True:
    print(contador)
    contador+= 1
    if contador==5:
        break
#Continue 
# se utiliza para saltar el resto del bloque de codigo dentro de un bucle y pasar a la siguiente itireracion
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)
#Pass 
# pass es una operacion nula que no hace nada. se utiliza como marcador de posicion cuando se requiere una instruccion sintacticamente ,  pero no se desea realizar ninguna accion.
for i in range(5):
    pass
    
