import time
import sys

valor_de_niño = 3000
valor_de_adulto = 6000
valor_de_adulto_mayor = 4000
valor_total = 0
contador_de_niño = 0
contador_de_adulto = 0
contador_de_adulto_mayor = 0
dinero_acumulado = 0

print ("/=========================/")
print ("/=======Cine kawaii=======/")
print ("/=========================/")

print ("Bievenidos al Cine.")
print ("Ahora mismo hay una sola pelicula disponible.")

ver_pelicula = str(input("¿Desea ver la pelicula? (SI/NO) : ")).lower()
print ()
if ver_pelicula == "no":
    print ("Que tenga un buen día.")

elif ver_pelicula == "si":
    print ("Bien, ahora siganos.")
    time.sleep(3)
    print ()
    print ("A continuación le mostraremos el costo de cada entrada.")
    print ("Espere pacientemente.\n")
    time.sleep(2)

    print (f"1. Menores de edad (1 a 12 años) --> ${valor_de_niño}.")
    print (f"2. Adultos/Joven (13 a 64 años) --> ${valor_de_adulto}.")
    print (f"3. Adulto Mayor (65 a 99 años) --> ${valor_de_adulto}.\n")

    print ("Ahora diganme ¿Cuántas entradas van a comprar?\n")

    compras_de_entradas = int(input ("Ingrese la cantidad de entradas : "))
    print (f"Usted va a comprar {compras_de_entradas} entradas ")
    print ()

    while compras_de_entradas > 0 :
        edad_de_entradas = int(input("Ingrese a edad para confirmar la entradas : "))
        print ()

        if edad_de_entradas >= 1 and edad_de_entradas <=12:
            print (f"Entrada de ' Menor de edad ' coste de --> ${valor_de_niño}")
            contador_de_niño += 1 
            compras_de_entradas -= 1
            print (f"Una entrada para niños confirmada. ({contador_de_niño}).")
            dinero_acumulado = dinero_acumulado + valor_de_niño
            print (f"Entradas restantes ({compras_de_entradas})\n")

        elif edad_de_entradas >= 13 and edad_de_entradas <=64:
            print (f"Entrada de ' Adulto/Joven ' coste de --> ${valor_de_adulto}")
            contador_de_adulto += 1 
            compras_de_entradas -= 1
            print (f"Una entrada para Adulto/Joven confirmada. ({contador_de_adulto}).")
            dinero_acumulado = dinero_acumulado + valor_de_niño
            print (f"Entradas restantes ({compras_de_entradas}). \n")

        elif edad_de_entradas >= 65 and edad_de_entradas <=99:
            print (f"Entrada de ' Adulto Mayor ' coste de --> ${valor_de_adulto_mayor}")
            contador_de_adulto_mayor += 1 
            compras_de_entradas -= 1
            print (f"Una entrada para niños confirmada. ({contador_de_adulto_mayor}).")
            dinero_acumulado = dinero_acumulado + valor_de_niño
            print (f"Entradas restantes ({compras_de_entradas}). \n")

        else:
            print ("Ingrese una edad valida.")
            compras_de_entradas -= 1
            print (f"Entradas restantes ({compras_de_entradas})")

        
            
else:
    print ("Ingrese solo ' SI ' o '' NO ' .")


print ("Tenemos todos los datos.")
print ("Espere pacientemente.\n")

print ("CALCULANDO...")
time.sleep(5)

print ("Ya contamos con los datos a pagar.\n")
print ("Usted debe...\n")
time.sleep(2)

print (f"Usted debe de pagar un total de ${dinero_acumulado}")
valor_total = contador_de_niño + contador_de_adulto_mayor + contador_de_adulto
print (f"A causa de que son un total de ({valor_total}) entradas.")
print (f"Repartidas en ({contador_de_niño}) niño/niños, ({contador_de_adulto}) Adultos/Jovenes y ({contador_de_adulto_mayor}) adultos mayores.")

confirmar_pago = str(input(f"¿Desea confirmar el monto de ${dinero_acumulado}? (SI/NO) : ")).lower()

if confirmar_pago == "si":
    print ("Que disfrute de la pelicula.")

elif confirmar_pago == "no":
    print ("Bueno, que tenga un buen día.")

else:
    print ("Ingrese solo (SI/NO) para confirmar.")



