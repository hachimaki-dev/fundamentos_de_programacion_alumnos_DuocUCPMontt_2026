#El bucle for es un iterador determinado , es decir cuando sabes cuantas veces se debe ejecutar el codigo o cuando tienes una coleccion de elementos que quieres recorrer de principio a fin 
#En cambio el bucle While se ejecuta mientras la condicion sea verdadera , no necesariamente debes saber cuantas vueltas dara el bucle , se detendra cuando la condicion que haya puesto se dejo de cumplir 
#Ejemplo 

#servidores_activos = [101 , 105 , 108 , 112]
#servidor_buscado = 105 

#for server in servidores_activos:
    #if server == servidor_buscado :
        #print(f"Servidor{servidor_buscado}encontrado en la red")
        #break #Encontro el dato , rompe el ciclo
#else: 
    #print(f"Error : el servidor {servidor_buscado} esta inactivo o no existe")    
    #Solo se ejecuta cuando el "for" termino de revisar toda la lista sin hacer nada
    #Pd todavia no lo entiendo , debo de practicar en algun ejercicio 
objeto_registrado=["Tijeras" , "Hojas" , "Correctores"]
for objeto in objeto_registrado :
    if objeto == objeto_registrado :
        print(f"{objeto_registrado}fue encontrado {objeto}")
        break