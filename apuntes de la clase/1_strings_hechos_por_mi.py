#IMPRESIONES SENCILLAS 
print("mi primer programa de python")

print()

print("buenas tarde amigo: ")


#caracters especiales como \n = "nueva linea" o \t = "tabulacion" ejemplos:
print("1- linea 1\nLinea 2\nLinea 3")
print("2- que\npasa\nlos\ncabros")# y en la consola se muestra separado en 3 lineas
#ejemplos usando \t = tabulacion: espacio largo y ya 
print("3- bueno que pasa: \tnada :c")
print("4- hola como estas ?\tbien aca estamos c:")
print("")
print("")
print("")

#IMPRESIONES CON SEPARADORES: sep= " espacio" o " / " o " . " y usando: " , " asi se define que va entre cada valor. aca algunos ejemplos:
print("1- yo ", "amo", "a", "mi", "madre", sep=" ") #usando el separador de "espacio"
print("2- queiro", "aprender", "mucjo ", "mas", sep="/") #usando el separador de " "" "
print("3- aca", "uso", "el","separador", "de: "  " . ",sep=".")#usando el separador de " . "
print("4- tambien", "se ", "puede", "usar", "el ","separador ", " de: , " "como si de IP se tratara", sep=",")
# CON ALT + A es para reducir el codigo para mas visibilidad


#IMPRESIONES USANDO END: define que va al final del print:
#aca estos 3 print se juntan y forman solo una linea en la consola
print("espera", end="")
print("..... ya casi" "..........", end="")
print(" estamos ready c:")

#combianando las 3 funciones de print:
print("buenos dias" "\t.......amaneci super bien", sep="," "|" , end= " \tya estoy cansado adios")
print("")
print("")

#MAS PRINTS y sys.stdout:
#mas formas de imprimir en la consola
#sys.stdout es la salida "estandar" del sistema.

#arte de ASCII = DIBUJOS CON TXT: 
print("QUE ES UN ASCII?:  ")
print("""  
      
       |------------------- |
       |      |--------|    |  
       |      |        |    | <------------- "eso es un ASCII basicamente son dibujitos "
       |      |--------|    |
       |--------------------|
      """)
#ARTE DE IMPRIMIR UN EMOJI ES USANDO SU UNICODE EJ:
print("😫😃😃😃😃😃😃😃😃😃")
print("")

#multiplicar string usando el: " * "
print(" I" * 50)
print("nose que poner aca c:" * 3)
print("por que sera ?" * 4)
print("")

#hay que importar el "sys":
import sys
# --- sys.stdout.write: escritura directa (sin salto de línea automático) 
# lo que si para saltar de linea se agrega el  "\n"
#es mejor este tipo de funcion por que usa menos  recursos, los juegos en las patallas de carga
sys.stdout.write("Esto se escribe con sys.stdout.write\n")
sys.stdout.write("No agrega salto de línea automático, ")
sys.stdout.write("así que todo queda en la misma línea.\n")

sys.stdout.write("nose pero tengo que agregar un ejemplo de:\n")
sys.stdout.write("sys.stdout.write y le damos para saltar de linea")
sys.stdout.write(" " "aca saltamos de linea de una jeje\n")
print("")

#imprimir caracter especiales literales con r"" (raw string)
print(r"asi que esto es un raw string: el\n no hace el salto de linea")
print(r"ruta de un archivo ? C: meh")
print("ni idea no lo entendi muy bien el raw string c:")
print("")

#impresion usando los formatos de: center() , ljust() , rjust() 
#para ordenar los txt y darle posiciones y lugares determinados como listas etc...
titulo = "NOMBRES DE LOS LOCOS Y APELLIDOS"
fin = "nombre y apellidos de los pelafustan jeje"
print(titulo.center(60, "="))
print("juanito".ljust(20, "-")+ "perez")
print("bastian".ljust(20, "-")+ "rodriguez")
print("matias".ljust(20, "-")+ "gonzales")
print(fin.center(60, "="))





