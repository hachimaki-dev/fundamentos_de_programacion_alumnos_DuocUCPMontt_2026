""" Ejercicio 4 — Nombre de usuario para una app bancaria
Un banco digital pide al usuario crear un nombre de usuario. Las reglas son:

Mínimo 6 caracteres
Sin espacios
Si no cumple, muestra:

"Nombre inválido. Debe tener al menos 6 caracteres y no contener espacios."
Ejemplos válidos: juanp23, mariatorres, cliente99 Ejemplos inválidos: juan, maria torres, ok

Cuando sea válido:

"Usuario creado: juanp23" """

contador = 0
while contador == 0 :
    nombre = input("ingresa un nombre minimo 6 caracters y sin espacios: ")
    tamano_minimo = len(nombre)
    if len(nombre) >=6 and " " not in nombre:  
        print(f"usuario creado : {nombre} ")
        contador+=1
    else :
        print("respete las reglas e ingrese lo solicitado")
        print(tamano_minimo)
