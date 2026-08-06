#11. Saludo Personalizado Crea saludar(nombre) que retorne el string "Hola, [nombre], bienvenido al sistema".
def saludar(nombre):
    return f"Hola , {nombre} ,bienvenido al sistema "
nombre1 = saludar("pedro")
print(nombre1)

#2. Calculadora Simple Crea sumar(a, b) que retorne la suma de los dos números recibidos.
def calculadoraSumar(a,b):
    return a + b
resultado = calculadoraSumar(20,30)
print(resultado)

#3. Número Par Crea es_par(numero) que retorne True si el número es par, y False si es impar.
def es_par(numero):
    if numero % 2 == 0:
        return True
    return False
numero1 = es_par(3)
print(numero1)

#4. Mayor de Tres Crea mayor_de_tres(a, b, c) que reciba 3 números y retorne el mayor de ellos.
def mayor_de_tres(a, b, c):
    if a > b or c:
        return a
    elif b > a or c:
            return b
    return c
resultado = mayor_de_tres(20,30,60)
print(resultado)

#5. . Contador de Vocales Crea contar_vocales(texto) que reciba un string y retorne la cantidad de vocales que contiene.
def contar_vocales(texto):
    return len(texto)
palabra = contar_vocales("paralelepipedo")
print(f"cantidad de vocales {palabra}")

#6. Reversa Crea reversar_texto(texto) que devuelva el string al revés. (Ej: "hola" -> "aloh")
def reversar_texto(texto):
     return texto[::-1]
texto_invertido = reversar_texto("jeje")
print(texto_invertido)

#7. Calculadora de Propinas Crea calcular_propina(total, porcentaje=10) que retorne el monto de la propina. El porcentaje por defecto es 10%.
def calcular_propina(total, porcentaje=10):
    resultado = total + total * porcentaje
    return resultado
propina = calcular_propina(10000)
print(propina)

#8. Filtrar Pares Crea filtrar_pares(lista_numeros) que reciba una lista, y retorne una NUEVA lista solo con los números pares.
def filtrar_pares(lista_numeros):
    nueva_lista = []
    for numeros_pares in lista_numeros:
        if numeros_pares % 2 == 0:
            nueva_lista.append(numeros_pares)
    return nueva_lista
lista_numeros = [1,2,3,4,5,6,7,8,9,10]
lista_cambiada = filtrar_pares(lista_numeros)
print(lista_cambiada)

#9. Conversor de Temperaturas Crea celsius_a_fahrenheit(c) que retorne la temperatura en F. Fórmula: (C * 9/5) + 32.
def celsius_a_fahrenheit(c):
    convercion = (c * 9/5) + 32
    return convercion
grados_a_medir = celsius_a_fahrenheit(20)
print(grados_a_medir)

#10. Generador de Password Crea generar_password(longitud=8) que retorne un string aleatorio de la longitud especificada.

def  generar_password(longitud=8):
    import random
    caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    password = ""
    for _ in range(longitud):
        password += random.choice(caracteres)  
    return password
print(generar_password())    
print(generar_password(12))

#11. Diccionario de Frecuencias Crea contar_caracteres(texto) que retorne un diccionario donde las claves son las letras y los valores son la cantidad de veces que aparecen.
"""def contar_caracteres(texto):
    """

#12. Validador de Email Crea es_email_valido(email) que retorne True solo si el texto contiene al menos un "@" y un "."
def es_email_valido(email):
    if "." in email and "@" in email:
        return True
    return False
email1 = es_email_valido("josenana@gmail.com")
print(email1)

# 13. Promedio de Lista Crea promedio(lista) que retorne el promedio de una lista de números. Retorna 0 si la lista está vacía.
def promedio(lista):
    if len(lista) > 0:
        total = sum(lista)
        cantidad = len(lista)
        return total / cantidad
    return 0
notas_alumnos = [1.0,7.0,7.0,3.3]
promedio_final = promedio(notas_alumnos)
print(promedio_final)

#14. Buscar en Diccionario Crea buscar_alumno(rut, diccionario_alumnos) que retorne el nombre del alumno si el rut existe, o "No encontrado" si no.
alumnos = {
    "12345678-9": "Juan Pérez",
    "18.765.432-1": "María Ortega",
    "20.123.456-k": "Carlos Muñoz",
    "15.987.654-3": "Ana Silva"
}
def buscar_alumno(rut, diccionario_alumnos):
    for rut_cada_alumno , nombre_alumno in diccionario_alumnos.items():
        if rut == rut_cada_alumno :
            return nombre_alumno
        return "no encontrado"
buscar_rut1 = buscar_alumno("12345678-9",alumnos)
print(f"el alumno encontrado es {buscar_rut1}")

# 15. Función Compuesta Usando filtrar_pares() y sumar(), crea sumar_pares_lista(lista) que reciba una lista y retorne la suma de todos los números pares en ella.
def filtrar_pares(lista):
    for numero_impares in lista:
        if numero_impares % 2 != 0:
            lista.pop(numero_impares)
            total = sum(lista)
            return total

def sumar(lista):
    return sum(lista)

notas_alumnos = [1,2,3,4,5,6,7,8,9,10]
resultado2 = filtrar_pares(notas_alumnos)
print(resultado2)