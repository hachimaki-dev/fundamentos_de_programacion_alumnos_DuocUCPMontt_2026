#VARIABLES parte 1:
#CREAR VARIABLES Y CONOCES TIPOS BASICOS 
#UNA VARIABLE ES COMO UNA CAJA DONDE GUARDAS UN DATO
#PYTHON DETECTA AUTOMATICAMNETE EL TIPO DE DATO 
print("VARIABLES parte 1:")
#varialbles basicas ej:
nombre = "juanito" # str (txt o cadena)
edad = 21          # int (numero entero)
altura = 1.89      # float (numero decimal)
es_estudiante = True # bool (verdadero o falso)
#se le puede asignar esos valores a una varible.

print("imprecion de variables: ")
#imprecion de variables
print("nombre:", nombre)
print("edad:", edad)
print("altura:", altura)
print("es estudiante ?", es_estudiante)
print("")


print("Verificar el tipo de cada variable con type: ")
# --- Verificar el tipo de cada variable con type() 
#da a mostrar en la consola que tipo de variable es: mostrando su nombre ej bool , str,float y int
print("Tipo de nombre:", type(nombre))
print("Tipo de edad:", type(edad))
print("Tipo de altura:", type(altura))
print("Tipo de es_estudiante:", type(es_estudiante))
print(" = " * 30)
print("")

print("VARIABLES parte 2:")
print("")
#VARIABLES PARTE 2:
#conversion de variables y asignacion multiple
#la nesecidad de convertir un tipo de dato en otro
#se puede asignar multiples variables en uno sola linea

#conversion de tipos (casting)
print("conversion de tipos: ")
numero_txt = "42"#al tener comillas el py lo lee como palabra el numero
numero_entero = int(numero_txt) #str a int
numero_decimal = float(numero_txt) #str a float

print("Texto original:", numero_txt, "| Tipo:", type(numero_txt))
print("Convertido a int:", numero_entero, "| Tipo:", type(numero_entero))
print("Convertido a float:", numero_decimal, "| Tipo:", type(numero_decimal))
#entender leyendo la consola.

print("convertir de numero a str")
#convertir de numero a str
valor = 8000
valor_txt = str(valor)
print("lo que vale "+ valor_txt) #para concatenar tienen que ser ambos str
#cocadenar el str con el int daria error ej:
#print("lo que valer " + valor) 
print("")

print("assignacion multiple: ")
#assignacion multiple.# le asigne valores a multiples variables en una sola linea de codigo:
a, b, c = 5, 10, 15
print("a =", a, "| b =", b,"| c =",c )
print("")

print("mismo valor en multiples variables")
#mismo valor en multiples variables:
a = b = c = 0
print("a =", a, "| b =", b,"| c =",c )

print("intercambiar valores (swap = cambio): ")
#intercambiar valores (swap = cambio)
inicio = "toronja"
final = "manzana"
print("antes: inicio = ", inicio, "| final =",final)
inicio, final = final, inicio #python hace el cambio cruzado de valores
print("ahora: inicio =", inicio, "| final =", final)
print("")

print("reasignar valores (cambio de su valor y tipo):")
#reasignar valores (cambio de su valor y tipo):
numero = 1000
print("numero = ", numero, "| tipo: ", type(numero))
numero = "ahora es txt o str"
print("numero = ", numero, "| tipo: ", type(numero))
numero = 3.3
print ("numero = ", numero, "| tipo o type", type(numero))
#en el "FLOAT" el valor de decimal se asigna con el punto: " . "
print("")
print(" = " * 30)

print("VARIABLES Y TIPOS DE DATO PARTE 3: ")
print("")
#VARIABLES Y TIPOS DE DATO 
import sys 
print("id : donde se almacena el dato exacatamente fisicamente: ")
# direccion de memoria del objeto 
a = 50
b = 50 
c = 100 

print("a =", a, "| id(a) =", id(a))
print("b =", b, "| id(b) =", id(b))
print("c =", c, "| id(c) =", id(c))
print("¿a y b apuntan al mismo objeto?", a is b)  # True (Python optimiza enteros pequeños)
print("¿a y c apuntan al mismo objeto?", a is c)  # False (# "is" es para hacer comparaciones)
#el id es donde esta asignado fisicamente tal valor.
print("")
print("=" * 60)

print("valores descritos que tan pesados son para el sistema en bytes : sys.getsizeof:")
entero = 1 
decimal = 0.1
txt = ""
txt_largo = "no se que poner aca"
booleano = True 

print(f"tamaño de int(entero) (1):        {sys.getsizeof(entero)} bytes")
print(f"tamaño de float(decimal) (0.1):   {sys.getsizeof(decimal)} bytes")
print(f"tamaño de txt vacio  :       {sys.getsizeof(txt)} bytes")
print(f"tamaño de memoria de txt_largo: {sys.getsizeof(txt_largo)} bytes")
print(f"tamaño de memoria de (booleano) (true): {sys.getsizeof(booleano)} bytes")
#es el tamaño de memoria se usa el sys.getsizeof+laVariable 
print("")
print("=" * 60)

print("conveciones de constantes, python no tiene constantes reales")
# --- Convenciones de "constantes" (Python no tiene constantes reales) ---
PI = 3.14159265
GRAVEDAD = 9.81
VELOCIDAD_LUZ = 299_792_458  # Los guiones bajos mejoran la comprencion en números grandes 
#ademas de que se puede usar para mejor entendimiento 
print(f"PI = {PI} ademas de ser un float")
print(f"Gravedad = {GRAVEDAD} m/s² ademas de ser un float")
print(f"Velocidad de la luz = {VELOCIDAD_LUZ} m/s siendo un int" )
print("")
print("=" * 60)

print("separador de miles usando el: _  : ")
poblacion_de_pueblo = 1_000_0000
dinero = 5000
print(f"poblacion de la muni :{poblacion_de_pueblo:,} ") #formato con comas ?
print(f"dinero del pueblo: ${dinero:,.0f}") # forma especial de usar el "0" y el "F" large descripcion
print("")
print("=" * 60)

# --- None: la ausencia de valor ---
resultado = None
print("resultado =", resultado)
print("Tipo de None:", type(resultado))
print("¿resultado es None?", resultado is None)
#basicamnete "none" = nullo y ya









