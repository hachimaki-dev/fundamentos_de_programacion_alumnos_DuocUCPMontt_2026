Busco diseñar una clase práctica de 60 minutos enfocada en desarrollar pensamiento computacional mediante el uso intensivo de estructuras de control en Python, específicamente `while`, `if`, `break`, `continue` y operadores lógicos. Los estudiantes ya conocen la sintaxis básica, pero presentan dificultades al momento de decidir cuándo y cómo aplicar correctamente estas estructuras en conjunto, especialmente en escenarios donde intervienen condiciones compuestas y anidadas.

La estrategia pedagógica consiste en trabajar con “micro-ejercicios” o “micro-retos”, es decir, fragmentos de código muy breves que obliguen a razonar sobre el flujo del programa. Cada ejercicio debe centrarse en un concepto específico: ruptura de ciclos, salto de iteraciones, evaluación de condiciones lógicas o identificación de errores. El objetivo no es escribir mucho código, sino comprender profundamente qué ocurre en cada iteración.

Los ejercicios deben incluir interacción con el usuario mediante `input()` y `print()`, promoviendo una experiencia más concreta. Además, se busca que los estudiantes predigan el comportamiento del código antes de ejecutarlo, fomentando la simulación mental del programa. Esto es clave para fortalecer habilidades como trazabilidad, anticipación de resultados y detección de errores lógicos.

También es importante incorporar ejercicios con errores intencionales (por ejemplo, loops infinitos o condiciones mal ordenadas) para que los estudiantes identifiquen fallas en la lógica. La autoevaluación debe ser parte central de la actividad: cada estudiante debería poder ejecutar, comparar resultados y corregir su propio razonamiento sin depender completamente del docente.

Finalmente, la experiencia debe ser dinámica, iterativa y reflexiva, priorizando la comprensión del flujo de ejecución por sobre la memorización. Se busca que los estudiantes internalicen preguntas clave como: ¿cuándo se rompe el ciclo?, ¿qué condiciones realmente se están evaluando?, ¿qué líneas no se ejecutan nunca?, y ¿cómo influye el orden de las instrucciones en el resultado final?

---

### Ejemplos

```python
# Ejemplo 1: detenerse con una palabra clave
while True:
    palabra = input("Escribe una palabra (salir para terminar): ")
    if palabra == "salir":
        break
    print("Ingresaste:", palabra)
```

```python
# Ejemplo 2: saltarse un caso con continue
while True:
    numero = int(input("Ingresa un número (0 para salir): "))
    if numero == 0:
        break
    if numero % 2 == 0:
        continue
    print("Número impar válido:", numero)
```

```python
# Ejemplo 3: if anidado dentro de while
while True:
    edad = int(input("Edad (0 para salir): "))
    if edad == 0:
        break
    if edad >= 18:
        if edad >= 60:
            print("Adulto mayor")
        else:
            print("Adulto")
    else:
        print("Menor de edad")
```

```python
# Ejemplo 4: lógica proposicional con and
while True:
    nota = int(input("Nota (0 para salir): "))
    if nota == 0:
        break
    if nota >= 4 and nota <= 7:
        print("Aprobado")
    else:
        print("No aprobado")
```

```python
# Ejemplo 5: lógica proposicional con or
while True:
    respuesta = input("¿Deseas continuar? (si/no): ")
    if respuesta == "no" or respuesta == "n":
        break
    print("Seguimos...")
```

```python
# Ejemplo 6: bug intencional para detectar razonamiento
while True:
    numero = int(input("Ingresa un número (0 para salir): "))
    if numero % 3 == 0:
        continue
    if numero == 0:
        break
    print("Número aceptado:", numero)
```

```python
# Micro-reto: ¿cuántas veces imprime?
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)
```

```python
# Micro-reto: ¿en qué momento se rompe?
i = 0
while True:
    print(i)
    if i == 2:
        break
    i += 1
```

```python
# Micro-reto: predice la salida sin ejecutar
while True:
    texto = input("Escribe algo: ")
    if texto == "fin":
        break
    if texto == "":
        continue
    print("OK")
```
