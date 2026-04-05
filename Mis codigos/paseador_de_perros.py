import time
import sys

#valor de los perros

valor_perro_pequeño = 2000
valor_perro_mediano = 4000
valor_perro_grande = 6000
dinero_ganado = 0
perro_pequeño = 0
perro_mediano = 0
perro_grande = 0


print ("/==============================/")
print ("/======Paseador de Perros======/")
print ("/==============================/\n")


print ("Bienvenido a nuestro servicio.")
print ("Aquí podras paser a su perro y podra ganar una cantidad de dinero dependiendo el tiempo que lo paseo.")
print ("en unos minutso le mostramos un pequeño menú de instrucciones con respecto al dinero y peso del perro.\n")
time.sleep(2)

print ("Bien, ya puedes ver las instrucciones.\n")

print (f"1. Perro Pequeño (menos de 10 KG) --> ${valor_perro_pequeño}.")
print (f"2. Perro Mediano (entre 11 y 25 KG) --> ${valor_perro_mediano}.")
print (f"3. Perro Grande  (26 KG o más) --> ${valor_perro_grande}.\n") 

print ("Con esto mencionado, en la sección de abajo introduzca cuantos perros desea pasear.\n")

perro_paseados = int(input("Ingrese la cantidad de perros : "))
print (f"Bien, usted va a pasear un maximo de {perro_paseados} perros.")
print()

while perro_paseados > 0 :
    peso_de_perros = int (input ("Ingrese el peso de ellos :"))
    print ()
    
    if peso_de_perros  >= 1 and peso_de_perros <= 10:
        print (f"Usted esta paseando a un perro pequeño por lo que su ganacia es de {valor_perro_pequeño}.")
        perro_pequeño += 1
        perro_paseados -= 1
        print (f"Contador de perros pequeños. {perro_pequeño}.\n")
        print (f"Cantidad de Perros por pasear {perro_paseados}\n")
        dinero_ganado = dinero_ganado + valor_perro_pequeño

        print (f"SU GANANCIA ES DE ${dinero_ganado}")

    elif peso_de_perros >=11 and peso_de_perros <=25:
        print (f"Usted esta paseando a un perro mediano por lo que su ganacia es de {valor_perro_mediano}.")
        perro_mediano += 1
        perro_paseados -= 1
        print (f"Contador de perros mediano. {perro_mediano}.")
        print (f"Cantidad de Perros por pasear {perro_paseados}\n")
        dinero_ganado = dinero_ganado + valor_perro_mediano

        print (f"SU GANANCIA ES DE ${dinero_ganado}")

    elif peso_de_perros >=26 and peso_de_perros <=50 :
        print (f"Usted esta paseando a un perro grande por lo que su ganacia es de {valor_perro_grande}.")
        perro_grande += 1
        perro_paseados -= 1
        print (f"Contador de perros Grande. {perro_grande}") 
        print (f"Cantidad de Perros por pasear {perro_paseados}\n")
        dinero_ganado = dinero_ganado + valor_perro_grande

        print (f"SU GANANCIA ES DE ${dinero_ganado}")

    else:
        print ()
        print ("Ingrese un peso valido. Maximo 50 KG.")
        perro_paseados -= 1
        print (f"Cantidad de Perros por pasear {perro_paseados}\n")

print ()
print ("Bien, has paseado a todos los perros, ahora es momento de calcular todo.")
print ("Espere pacientemente. \n")
print ("CALCULANDO... \n")
time.sleep(5)


print ("/==============================/")
print ("/=========Fin del día/=========/")
print ("/==============================/\n")

print ("Felicidades.")
print (f"El dinero que usted ha ganado es de {dinero_ganado}\n")

total_de_perros = perro_grande + perro_mediano + perro_pequeño
print (f"Usted ha paseado una cantidad de {total_de_perros} perros en total.")
print ("BUEN TRABAJO U.U")








