""" Ejercicio 1B — Registro de pasajeros en un vuelo

Una aerolínea necesita saber cuántos pasajeros abordaron un vuelo. 
El número debe ser mayor que cero (no puede haber un vuelo con cero o menos 
pasajeros).

Escribe un programa que pida el número de pasajeros 
y que no avance hasta recibir un entero positivo. Si el dato es inválido, 
muestra:
"Error: ingresa un número entero positivo de pasajeros."

Cuando el dato sea válido, muestra el valor que el usuario ingresó:
"Vuelo registrado con {pasajeros} pasajeros."
(Ejemplo: si el usuario ingresa 142, se muestra 
"Vuelo registrado con 142 pasajeros.")

Casos de prueba que debes intentar: 0, -5, "abc", 3.7, 200 """
contador = 0
while contador < 1:
    try:
        numero_de_pasajeros = int(input("ingresa el numero de pasajeros"))
        if numero_de_pasajeros > 0:
            contador +=1
            print(f"valuelo registrado con {numero_de_pasajeros} pasajeros")
        else:
            print("ingresa un numero real")
            
    except ValueError :
        print("ingresa un numero valido")