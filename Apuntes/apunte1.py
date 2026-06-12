def saludar(nombre):
    print(f"Hola {nombre}") #Imprime directamente el texto colocado.

resultado = saludar("Ana") #Funciona para llamar la función, evaluandola internamente para luego entregar la información a la variable.
print(resultado)












def doble(x):
    return x * 2

a = doble(5)
b = doble(doble(3))
print(a, b)











x = 10

def cambiar():
    x = 99
    return x

resultado = cambiar()
print(x)
print(resultado)
  









#¿Qué es una función?: Una función es eso: un bloque de código con un nombre. Lo defines UNA vez, lo invocas las veces que quieras.
#ejemplo: Imagina que cada vez que quieres lavarte los dientes tuvieras que explicar: «agarra el cepillo, pon pasta, mueve la mano, enjuaga...»

def lavarse_dientes():
    print("Agarrar cepillo")
    print("Cepillar 2 minutos")

lavarse_dientes()  # invocación
lavarse_dientes()  # se puede usar cuantas veces quieras









#Definir: Escribir el código con def
#Invocar: Ejecutar con nombre()
#Parámetro: Variable en la definición
#Argumento: Valor real al invocar

def lavarse_dientes(minutos):  # "minutos" es PARÁMETRO
    print(f"Cepillando por {minutos} minutos")

lavarse_dientes(2)  # "2" es el ARGUMENTO








#Muestra algo en pantalla. Solo para el humano. El programa NO puede usarlo después.
#Entrega un valor al programa. Comunicación entre funciones. El programa SÍ puede usar ese valor.

def sumar_print(a, b):
    print(a + b)     # solo IMPRIME, no entrega nada

def sumar_return(a, b):
    return a + b     # ENTREGA el resultado

resultado1 = sumar_print(3, 4)    # en pantalla: 7
print(resultado1)                    # pero esto imprime: None !!

resultado2 = sumar_return(3, 4)   # no aparece nada en pantalla
print(resultado2)                    # esto imprime: 7
  



def saludar(nombre, idioma="español"):
    if idioma == "español":
        print(f"Hola, {nombre}")
    elif idioma == "inglés":
        print(f"Hello, {nombre}")

saludar("Juan")              # usa "español" por defecto
saludar("John", "inglés")    # sobreescribe el default
  








#Listas y Dicts (mutables) Se pasan «por referencia». La función modifica el original. .append() cambia la lista de afuera.
# Números y Strings (inmutables) Se pasan «por valor». La función recibe una copia. El original no cambia.


# LISTA: el cambio SÍ se mantiene afuera
def agregar_fruta(lista_frutas):
    lista_frutas.append("manzana")  # sin return

mis_frutas = ["pera", "uva"]
agregar_fruta(mis_frutas)
print(mis_frutas)  # ['pera', 'uva', 'manzana'] ✅

# NÚMERO: el cambio NO se mantiene afuera
def intentar_cambiar(numero):
    numero = numero + 100

x = 5
intentar_cambiar(x)
print(x)  # sigue siendo 5 ❌
  








#Funciones de Validación


# Versión Pythónica

def es_mayor(edad):
    return edad >= 18

# Versión Explícita

def es_mayor(pene):
    if edad >= 18:
        return True
    else:
        return False