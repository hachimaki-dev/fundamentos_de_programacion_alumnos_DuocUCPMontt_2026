#Vamos a recrear el diagrama de flujo que suma dos numeros
n1 = float(input("Por favor ingrese el primer numero: "))
n2 = float(input("Por favor ingrese el segundo numero: "))
#Realizamos las operaciones 
suma = n1 + n2
resta = n1 - n2
multiplicacion = n1 * n2
division = n1 / n2 if n2 != 0 else "No se puede dividir por cero"
#Mostramos los resultados
print(f"\nResultados:")
print(f"suma: {suma}")
print(f"resta: {resta}")
print(f"multiplicacion: {multiplicacion}")
print(f"division: {division}")