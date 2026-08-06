#INPUTS PARTE 2 
#CONVERCION DE INPUTS Y HACER CALCULOS 
#COMO INIPUT SIEMPRE DEVUELVE STR , SE DEBE CONVERTIR A INT O FLOAT PARA HACER 
#OPERACIONES MATEMATICAS.
print("input PARTE 2: convercion de str a float o int(decimal o N )")

print("=" * 20 + "CALCULADORA DE EDAD" + "=" * 20)
nombre = input("ingresa tu edad: ")
año_de_nacimiento = int(input("ingresa tu año de nacimiento: "))

edad = 2026 - año_de_nacimiento
print(f"{nombre} la edad que tienes o cumpliras es: {edad} años en 2026 ")
#BUEN EJ DE CONTATENACION DE STR Y VALORES USANDO EL "F" 
print("")

print(f"="*20, "calculadora de promedio", "="*20)

nota1 = float(input("ingresa tu nota 1: "))
nota2 = float(input("ingresa tu nota 2: "))
nota3 = float(input("ingresa tu nota 3: "))

promedio = (nota1 + nota2 + nota3) / 3 #recuerda que el promedio es dividido por sus valores de suma
print(f"tu promedio general es: {promedio:.1f}")
#en la funcion de "promedio:.1f" el punto 1 " .1 " cumple la funcion de dar un decimal 
# y la "f" es de float.

peso = float(input("Ingresa tu peso en kg: "))
altura = float(input("Ingresa tu altura en metros (ej: 1.75): "))

imc = peso / (altura ** 2)
#imc = indice masa corporal
print(f"Tu IMC es: {imc:.2f}")