valor_normal = 800
valor_estudiantes = 250
dinero_acumulado = 0
contador_normal = 0
contador_estudiantes = 0
contador_final = 0

print ("1.(N) Pasaje Normal" + f"${valor_normal}" )
print ("2.(E) Pasaje Estudinates"   + f"${valor_estudiantes}")
print ("3.(C) corte \n")


Numero_de_pasajero = int(input("¿Cuántos pasajero son : "))

while True :
    eleccion_de_pasajero = str(input("Ingrese (N) y (E) para confirmar su pasaje : ")).lower()
    
    if eleccion_de_pasajero == "n" :
        print (f"Usted ha seleccionado el pasaja de {eleccion_de_pasajero} por lo tanto se le cobra un total de {valor_normal}")
        dinero_acumulado = dinero_acumulado + valor_normal
        contador_normal += 1
        print (f"el dinero acumulado es {dinero_acumulado}\n")

    elif eleccion_de_pasajero == "e" :
        print (f"Usted ha seleccionado el pasaja de {eleccion_de_pasajero} por lo tanto se le cobra un total de {valor_estudiantes}")
        contador_estudiantes += 1
        dinero_acumulado = dinero_acumulado + valor_estudiantes
        print (f"el dinero acumulado es {dinero_acumulado}\n")

    else :
        print (" ' ERROR ' , Ingrese solo (N) o (E)")

print ("Se ingreso corte")
        


        




print ("Todos los estudiantes han hecho sus vots.")
print ("Por favor esperen que estamos valinado cada uno de ellos")
time.sleep(5)


