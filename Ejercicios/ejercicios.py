import sys
#Ejercicio 1
def OPCION():
    while True:
        respuesta = input("¿Seguir? (Responder con si o no): ").lower()
        if respuesta == "si":
            print("Continuamos")
            break
        elif respuesta == "no":
            print("Perfecto, entonces salimos")
            sys.exit()
        else:
            print("Escriba una opción válida")
saludo = "Hola Mundo"
print(saludo)
saludo = ""
OPCION ()
#Ejercicio 2
total = (15 + 25) * 2
print(total)
OPCION ()
#Ejercicio 3
estado = ""
nota = 4.0
if nota >= 4.0:
    estado = "Aprobado"
else:
    estado = "Reprobado"
print(nota)
print(estado)
OPCION ()
#Ejercicio 4:
suma = 0
contador = 1
while True:
    suma = suma + 1
    print(suma)
    contador = contador + 1
    if contador == 6:
        break
OPCION ()
#Ejercicio 5
total = 0
for i in range (11):
    total = total + i
    print(total)
OPCION ()
#Ejercicio 6
contador_a = 0
for letra in ("Palabra"):
    if letra == "a":
        contador_a = contador_a + 1
        print(f"Hay {contador_a} a")
OPCION ()
#Ejercicio 7
lista = [
    "Espada",
    "Escudo",
    "Pocion"
]
for palabra in lista:
    print(palabra)
OPCION ()
#Ejercicio 8
lista = [
    "Espada",
    "Escudo",
    "Pocion"
]
for palabra in lista:
    print(palabra)
print("Se agrego mapa")
lista.append("mapa")
for palabra in lista:
    print(palabra)
#Ejercicio 9
total = 0
print("Los precios son $1000, $2500 y $500")
print("Es total a pagar se llevara a cabo con una listay el uso de FOR")
precios = [
    1000,
    2500,
    500
]
for precio in precios:
    total = total + precio
print(f"El total a pagar es de ${total}")
OPCION ()
#Ejercicio 10
perfil = {
    "nombre": "Ash",
    "edad": 10
}
print("Nombre", perfil["nombre"])
print("Edad", perfil["edad"])
OPCION ()
#Ejercicio 11
enemigo = {
    "nombre": "Slime",
    "HP": 45
}
print("Nombre", enemigo["nombre"])
HP_ACTUAL = "HP Actual", enemigo["HP"]
print(HP_ACTUAL)
OPCION ()
#Ejercicio 12
ventas = [
    {"Clave": "Laptop", "Valor": 15, "Precio": 399990},
    {"Clave": "Mouse", "Valor": 30, "Precio": 9990}
]

total = 0

for venta in ventas:
    print(venta["Clave"], venta["Valor"], venta["Precio"])
    total = total + venta["Valor"] * venta["Precio"]

print("Total:", total)
OPCION ()
#Ejercicio 13
edades = [
    15, 18, 22, 12, 40
]
contador = 0
for edad in edades:
    print(f"La edad es de {edad}")
    if edad >= 18:
        contador = contador + 1
print(f"Hay {contador} personas mayores de edad")
#Ejercicio 14
nombres = ""
contador = 0
alumnos = [
    {"Nombre": "Martin", "Nota": 5.0},
    {"Nombre": "Alexander", "Nota": 3.5},
    {"Nombre": "Hector", "Nota": 5.0}
]
for alumno in alumnos:
    print(alumno["Nombre"], alumno["Nota"])
    if alumno["Nota"] > 4.0:
        nombres = nombres + alumno["Nombre"] + "," + " "
        contador = contador + 1
print(f"Pasaron {contador}: {nombres}")
OPCION ()
#Ejercicio 15
total = 0
tienda = [
    {"pocion": {"precio": 500, "stock": 15}},
    {"espada": {"precio": 300, "stock": 30}}
]
for item in tienda:
    for nombre, datos in item.items():
        print(nombre, datos)
        total = total + datos["precio"] * datos["stock"]
while True:
    respuesta = input("Deseas saber el total (responder con 'si' o ¿no')").lower()
    if respuesta == "si":
        print(f"Perfecto, el total seria de: {total}")
        break
    elif respuesta == "no":
        print("Perfecto, pasamos al siguiente ejercicio")
        break
    else:
        print("Ingrese una respuesta valida")
OPCION ()
#Ejercicio 16
contador_a = 0
contador_b = 0
votos = [
    "A", "B", "A", "A", "B", "A", "A", "B", "A", "A"
]
for voto in votos:
    if voto == "A":
        contador_a = contador_a + 1
    elif voto == "B":
        contador_b = contador_b + 1
print(f"{contador_a} votaron por A y {contador_b} por B")
OPCION ()
#Ejercicio 17
jugadores = [
    {"nombre": "Martin", "Puntos": 20},
    {"nombre": "Alexander", "Puntos": 29},
    {"nombre": "Hector", "Puntos": 34}
]
mayor = 0
ganador = ""
for jugador in jugadores:
    print(jugador["nombre"], jugador["Puntos"])
    if jugador["Puntos"] > mayor:
        mayor = jugador["Puntos"]
        ganador = jugador["nombre"]
print(f"el ganador es {ganador} con {mayor} puntos")
OPCION ()
#Ejercicio 18
par = 0
inpar = 0
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9,
          10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
          20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
for numero in numeros:
    print(numero)
    if numero % 2:
        par = par + 1
    else:
        inpar = inpar + 1
print(f"Hay {par} pares y {inpar} inpares")
OPCION ()
#Ejercicio 19
contador = 0
compras = [
]
total = 0
ventas = [
    {"Clave": "1. Laptop", "Precio": 399990},
    {"Clave": "2. Mouse", "Precio": 9990},
    {"Clave": "3. Teclado", "Precio": 9990}
]
while True:
    for producto in ventas:
        print(producto["Clave"], producto["Precio"])
    print("4. Salir y ver monto")
    print("Con un total superior a $500.000 se obtiene un 10% de descuento")
    compra = input("¿Que desea comprar? (seleccionar del 1 al 3)")
    if compra == "1":
        print("Perfecto")
        compras.append("Laptop")
    elif compra == "2":
        print("Perfecto")
        compras.append("Mouse")
    elif compra == "3":
        print("Perfecto")
        compras.append("Teclado")
    elif compra == "4":
        print("Perfecto")
        break
    else:
        print("Seleccionar una opción válida")
for compra in compras:
    contador = contador + 1
    print(f"El articulo {contador} es {compra}")
    if compra == "Laptop":
        total = total + 399990
    elif compra == "Mouse":
        total = total + 9990
    elif compra == "Teclado":
        total = total + 9990
if total > 499999:
    print(f"El total de compra es de ${total} CLP")
    print(f"FELICIDADES!!! haz obtenido un 10% de descuento, su total es de ${total * 0.9}CLP")
else:
    print("Lastimosamente no tienes un descuento debido a que su total no llego a la cantidad necesaria")
    print(f"Su total es de {total}")
OPCION ()
#Ejercicio 20
catalogo = {
    "armas": ["espada", "arco", "hacha"], 
    "pociones": ["luz", "mana", "vida"]
}

stock = []

for tipo in catalogo:
    for nombre in catalogo[tipo]:
        print(nombre)
        if len(nombre) > 4:
            stock.append(nombre)

print(stock)