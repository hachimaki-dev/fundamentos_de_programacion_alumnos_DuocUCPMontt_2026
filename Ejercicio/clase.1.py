curso = ['benja',20, 'marron','barbara', 20,'negro']
curso_nombre = ['benja', 'barbara', 'diego']
curso_edad = [18, 18, 19]
curso_ojos = ['cafe', 'cafe', 'cafe']

print(f"nombre : {curso_nombre[0]}")
print(f"edad : {curso_edad[0]}")
print(f"ojos : {curso_ojos[0]}")

print(f"nombre : {curso_nombre[1]}")
print(f"edad : {curso_edad[1]}")
print(f"ojos : {curso_ojos[1]}")

print(f"nombre : {curso_nombre[2]}")
print(f"edad : {curso_edad[2]}")
print(f"ojos : {curso_ojos[2]}")

print(f"el tamaño de la lista de nombre es: { len (curso_nombre)}")

contador = 0
for nombre in curso_nombre :
    contador = contador + 1
    print(f"curso_nombre {contador} es {nombre}")