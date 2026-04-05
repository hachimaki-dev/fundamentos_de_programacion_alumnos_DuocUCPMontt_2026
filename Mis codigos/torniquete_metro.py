import time 
import sys

print ("/============================/")
print ("/=========Torniquete=========/")
print ("/============================/\n")

print ("Bienvenido al Metro de Santiago.")
print ("Aquí podras viajar de manera segura y con un espacio bastante grande.")
print ("En unos segundos le mostramos el cobro de los pasajes.\n")
time.sleep(2)


valor_normal = 800
valor_estudiantes = 450
valor_adulto_mayor = 250
dinero_acumulado = 0
contador_normal = 0
contador_estudiantes = 0
contador_adulto_mayor = 0
contador_final = 0

print (f"1.(N) Pasaje Adulto ${valor_normal}." )
print (f"2.(E) Pasaje Estudinates ${valor_estudiantes}.")
print (f"3 (A) Pasaje Adulto Mayor ${valor_adulto_mayor}.")
print ("4.(C) Corte o Salir. \n")

print ("Esos serían los valores de cada pasaje.")
print ("Ahora Por favor ingrese su pasaje en la sección de abajo.\n")
print ("QUE TENGA UN BONITO VIAJE U.U\n")



while True:
    eleccion_de_pasajero = str(input("Ingrese (N) y (E) para confirmar su pasaje : ")).lower()
    
    if eleccion_de_pasajero == "n" :
        print (f"Usted ha seleccionado el pasaja de 'Adulto' por lo tanto se le cobrara un total de {valor_normal}")
        contador_normal += 1
        dinero_acumulado = dinero_acumulado + valor_normal
        print (f"el dinero acumulado es {dinero_acumulado}\n")


    elif eleccion_de_pasajero == "e" :
        print (f"Usted ha seleccionado el pasaja de 'Estudiante' por lo tanto se le cobrara un total de {valor_estudiantes}")
        contador_estudiantes += 1
        dinero_acumulado = dinero_acumulado + valor_estudiantes
        print (f"el dinero acumulado es {dinero_acumulado}\n")


    elif eleccion_de_pasajero == "a":
        print (f"Usted ha seleccionado el pasaje 'Adulto Mayor' por lo que se le cobrara un total de {valor_adulto_mayor}")
        contador_adulto_mayor += 1
        dinero_acumulado = dinero_acumulado + valor_adulto_mayor
        print (f"el dinero acumulado es {dinero_acumulado}\n")


    elif  eleccion_de_pasajero == "c":
            break

    else :
        print (" ' ERROR ' , Ingrese solo (N) , (E) , (A) o (C)")


print ()
print ("SE INGRESO CORTE\n")
print ("REUNIENDO DATOS...\n")
time.sleep(4)
print ("Ya se han reunido los datos, ahora solo falta calcularlos\n")

print ("CALCULANDO DATOS...\n")
time.sleep(6)
    
print (f"El total de pasajeros estudiantes es de {contador_estudiantes}")
print (f"El total de pasajeros Adulto es de {contador_normal}")
print (f"El total de pasajero Adultos Mayores es de {contador_adulto_mayor}\n")

contador_final = contador_estudiantes + contador_normal + contador_adulto_mayor

print (f"El total de pasajeros fue de {contador_final}")
print (f"El dinero recaudado es de {dinero_acumulado}")



