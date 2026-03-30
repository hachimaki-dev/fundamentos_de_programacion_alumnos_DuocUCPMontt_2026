# 🔄 El Ciclo `for` en Python — Guía Completa para Estudiantes

> **Prerequisitos:** Variables, `input()`, `print()`, `if/elif/else`, `while`, operadores, `str`.
>
> **Lo que NO veremos hoy:** Listas, `enumerate`, doble `for`, diccionarios.

---

## 📌 ¿Qué es un `for`?

Un `for` **recorre una secuencia de valores que Python le entrega, uno por uno**.

No es "repetir X veces" (eso es una consecuencia, no la definición).
No es "recorrer listas" (eso vendrá después).

Es como una cinta transportadora 🏭: Python pone valores en la cinta, y el `for` los toma uno a uno.

```
  range(5) genera:  0 → 1 → 2 → 3 → 4
                    ↓   ↓   ↓   ↓   ↓
  el for toma:      i   i   i   i   i
                    y ejecuta el bloque con cada valor
```

---

# 🟦 NIVEL 1 — `for` con `range()`: Lo Básico

## 🎯 Concepto

`range(n)` genera una secuencia de números desde `0` hasta `n-1`.

```python
for i in range(5):
    print(i)
```

**Salida:**
```
0
1
2
3
4
```

### 🔍 Desglose línea por línea

| Vuelta | Valor de `i` | ¿Qué imprime? |
|--------|-------------|----------------|
| 1ª     | 0           | `0`            |
| 2ª     | 1           | `1`            |
| 3ª     | 2           | `2`            |
| 4ª     | 3           | `3`            |
| 5ª     | 4           | `4`            |

### 🌍 Ejemplo de la vida real: Cuenta regresiva de un microondas

```python
for segundo in range(5):
    print(f"Quedan {5 - segundo} segundos...")
print("🔔 ¡LISTO!")
```

**Salida:**
```
Quedan 5 segundos...
Quedan 4 segundos...
Quedan 3 segundos...
Quedan 2 segundos...
Quedan 1 segundos...
🔔 ¡LISTO!
```

### 💡 Nota importante: `i` NO es solo un "contador"

A veces no necesitas el valor de la variable. En ese caso, Python usa `_` por convención:

```python
for _ in range(3):
    print("¡Bienvenido!")
```

Esto imprime "¡Bienvenido!" tres veces. El `_` significa: "sé que hay un valor, pero no me importa cuál es".

---

## ✅ Chequeo de Comprensión — Nivel 1

### 🔘 Verdadero o Falso

| # | Afirmación | V/F |
|---|-----------|-----|
| 1 | `range(5)` genera los números del 1 al 5 | |
| 2 | La variable del `for` cambia automáticamente en cada vuelta | |
| 3 | `range(3)` genera exactamente 3 valores | |
| 4 | `for i in range(5):` ejecuta el bloque 5 veces | |
| 5 | El `for` necesita que tú incrementes `i` manualmente | |

<details>
<summary>📋 Ver respuestas</summary>

1. **FALSO** — Genera del 0 al 4 (5 valores, pero empieza en 0)
2. **VERDADERO** — Python la actualiza automáticamente
3. **VERDADERO** — Genera: 0, 1, 2
4. **VERDADERO** — Con i = 0, 1, 2, 3, 4
5. **FALSO** — Eso es en `while`. En `for`, Python lo hace solo

</details>

### 🔍 Encuentra el Error

```python
for i in range(4)
    print(i)
```

<details>
<summary>📋 Ver respuesta</summary>

Falta los **dos puntos** `:` al final de la línea del `for`:

```python
for i in range(4):  # ← aquí faltaba el :
    print(i)
```

</details>

---

```python
for i in range(3):
print(i)
```

<details>
<summary>📋 Ver respuesta</summary>

Falta la **indentación** (sangría) en el `print`:

```python
for i in range(3):
    print(i)  # ← debe tener 4 espacios de sangría
```

</details>

---

### ✍️ Completa el código que falta

**Objetivo:** Imprimir "Hola" exactamente 4 veces.

```python
___ _ in range(___):
    print("Hola")
```

<details>
<summary>📋 Ver respuesta</summary>

```python
for _ in range(4):
    print("Hola")
```

</details>

---

# 🟦 NIVEL 2 — Control del Rango: `inicio`, `fin`, `paso`

## 🎯 Concepto

`range()` puede recibir hasta 3 argumentos:

```
range(inicio, fin, paso)
```

| Forma | Qué genera | Ejemplo |
|-------|-----------|---------|
| `range(5)` | 0, 1, 2, 3, 4 | Solo `fin` |
| `range(2, 8)` | 2, 3, 4, 5, 6, 7 | `inicio` y `fin` |
| `range(1, 10, 2)` | 1, 3, 5, 7, 9 | `inicio`, `fin` y `paso` |
| `range(10, 0, -1)` | 10, 9, 8, ..., 1 | Cuenta regresiva |

⚠️ **Regla de oro:** El valor `fin` **NUNCA se incluye**.

### 🌍 Ejemplo de la vida real: Números de asiento en un bus

```python
# Asientos del 1 al 40
for asiento in range(1, 41):
    print(f"Asiento #{asiento}")
```

### 🌍 Ejemplo: Años bisiestos

```python
# Años bisiestos entre 2000 y 2030 (cada 4 años)
for anio in range(2000, 2031, 4):
    print(f"{anio} es bisiesto")
```

**Salida:**
```
2000 es bisiesto
2004 es bisiesto
2008 es bisiesto
...
2028 es bisiesto
```

### 🌍 Ejemplo: Cuenta regresiva de un cohete 🚀

```python
for i in range(10, 0, -1):
    print(i)
print("🚀 ¡DESPEGUE!")
```

---

## ✅ Chequeo de Comprensión — Nivel 2

### 🔗 Términos Pareados

Une cada expresión con su secuencia generada:

| # | Expresión | | Secuencia |
|---|-----------|--|-----------|
| A | `range(4)` | | `5, 4, 3, 2, 1` |
| B | `range(2, 6)` | | `0, 1, 2, 3` |
| C | `range(0, 10, 3)` | | `2, 3, 4, 5` |
| D | `range(5, 0, -1)` | | `0, 3, 6, 9` |

<details>
<summary>📋 Ver respuestas</summary>

- A → `0, 1, 2, 3`
- B → `2, 3, 4, 5`
- C → `0, 3, 6, 9`
- D → `5, 4, 3, 2, 1`

</details>

### 🔍 Encuentra el Error

```python
# Se supone que debe imprimir: 10, 8, 6, 4, 2
for i in range(10, 2, 2):
    print(i)
```

<details>
<summary>📋 Ver respuesta</summary>

El paso debe ser **negativo** porque vamos de 10 hacia abajo:

```python
for i in range(10, 0, -2):  # ← paso -2, y fin en 0 para incluir el 2
    print(i)
```

</details>

### 🔘 Verdadero o Falso

| # | Afirmación | V/F |
|---|-----------|-----|
| 1 | `range(1, 5)` incluye el número 5 | |
| 2 | `range(10, 0, -1)` genera una cuenta regresiva | |
| 3 | `range(0, 10, 2)` genera: 0, 2, 4, 6, 8 | |
| 4 | `range(5, 5)` genera un valor | |
| 5 | El tercer argumento de `range()` puede ser negativo | |

<details>
<summary>📋 Ver respuestas</summary>

1. **FALSO** — El `fin` nunca se incluye. Genera: 1, 2, 3, 4
2. **VERDADERO** — Genera: 10, 9, 8, 7, 6, 5, 4, 3, 2, 1
3. **VERDADERO** — Exacto
4. **FALSO** — inicio == fin, no genera nada (vacío)
5. **VERDADERO** — Se usa para contar hacia atrás

</details>

---

# 🟦 NIVEL 3 — Acumuladores: La Memoria del Ciclo

## 🎯 Concepto

Un **acumulador** es una variable que **guarda y actualiza un valor** a lo largo de las vueltas del ciclo.

```python
suma = 0  # ← Se inicializa ANTES del for

for i in range(1, 6):
    suma += i  # ← Se actualiza DENTRO del for

print(suma)  # ← Se usa DESPUÉS del for
```

### 🔍 Traza paso a paso

| Vuelta | `i` | `suma` antes | Operación | `suma` después |
|--------|-----|-------------|-----------|----------------|
| 1ª     | 1   | 0           | 0 + 1     | 1              |
| 2ª     | 2   | 1           | 1 + 2     | 3              |
| 3ª     | 3   | 3           | 3 + 3     | 6              |
| 4ª     | 4   | 6           | 6 + 4     | 10             |
| 5ª     | 5   | 10          | 10 + 5    | 15             |

**Resultado:** `15`

### 🌍 Ejemplo de la vida real: Caja registradora

```python
total = 0
cantidad_productos = 3

for i in range(1, cantidad_productos + 1):
    precio = int(input(f"Precio del producto {i}: $"))
    total += precio

print(f"Total a pagar: ${total}")
```

### 🌍 Ejemplo: Promedio de notas

```python
suma = 0
n = 4

for i in range(1, n + 1):
    nota = float(input(f"Ingrese nota {i}: "))
    suma += nota

promedio = suma / n
print(f"Promedio: {promedio:.1f}")
```

### 🌍 Ejemplo: Contador (otro tipo de acumulador)

```python
# ¿Cuántos números pares hay del 1 al 20?
contador = 0

for i in range(1, 21):
    if i % 2 == 0:
        contador += 1

print(f"Hay {contador} números pares")  # → Hay 10 números pares
```

---

## ✅ Chequeo de Comprensión — Nivel 3

### ✍️ Completa el código que falta

**Objetivo:** Calcular el producto de los números del 1 al 5 (factorial de 5 = 120).

```python
resultado = ___

for i in range(1, ___):
    resultado ___ i

print(resultado)
```

<details>
<summary>📋 Ver respuesta</summary>

```python
resultado = 1  # ← importante: para multiplicación se inicia en 1, no en 0

for i in range(1, 6):
    resultado *= i

print(resultado)  # → 120
```

</details>

### 🔍 Encuentra el Error

```python
# Se quiere sumar los números del 1 al 10
for i in range(1, 11):
    suma = 0
    suma += i

print(suma)
```

<details>
<summary>📋 Ver respuesta</summary>

El `suma = 0` está **DENTRO** del `for`, así que se reinicia en cada vuelta. Debe ir **ANTES**:

```python
suma = 0  # ← FUERA del for

for i in range(1, 11):
    suma += i

print(suma)  # → 55
```

**Este es el error #1 más común con acumuladores.**

</details>

### 🔘 Verdadero o Falso

| # | Afirmación | V/F |
|---|-----------|-----|
| 1 | Un acumulador de suma se inicializa en 0 | |
| 2 | Un acumulador de multiplicación se inicializa en 0 | |
| 3 | El acumulador debe inicializarse dentro del `for` | |
| 4 | `+=` es lo mismo que escribir `variable = variable + valor` | |

<details>
<summary>📋 Ver respuestas</summary>

1. **VERDADERO** — Porque sumar 0 no cambia el resultado
2. **FALSO** — Se inicializa en 1 (multiplicar por 0 da siempre 0)
3. **FALSO** — Debe inicializarse ANTES del `for`
4. **VERDADERO** — Es la forma abreviada

</details>

---

# 🟦 NIVEL 4 — Condicionales Dentro del `for`

## 🎯 Concepto

Puedes poner un `if` dentro del `for` para **filtrar**, **clasificar** o **decidir** qué hacer con cada valor.

```python
for i in range(10):
    if i % 2 == 0:
        print(f"{i} es par")
    else:
        print(f"{i} es impar")
```

### 🌍 Ejemplo de la vida real: Clasificar edades en una fila

```python
for i in range(1, 6):
    edad = int(input(f"Edad de la persona {i}: "))

    if edad < 18:
        print("  → Menor de edad")
    elif edad >= 65:
        print("  → Tercera edad")
    else:
        print("  → Adulto")
```

### 🌍 Ejemplo: Sistema de aprobación de notas

```python
aprobados = 0
reprobados = 0

for i in range(1, 6):
    nota = float(input(f"Nota alumno {i}: "))
    if nota >= 4.0:
        aprobados += 1
    else:
        reprobados += 1

print(f"\nAprobados: {aprobados}")
print(f"Reprobados: {reprobados}")
```

### 🌍 Ejemplo: Menú de cafetería con precios

```python
total = 0

for i in range(1, 4):
    print(f"\n--- Pedido {i} ---")
    opcion = input("¿Café (c) o Té (t)? ")

    if opcion == "c":
        total += 1500
        print("Café: $1500")
    elif opcion == "t":
        total += 1000
        print("Té: $1000")
    else:
        print("Opción no válida")

print(f"\nTotal: ${total}")
```

---

## ✅ Chequeo de Comprensión — Nivel 4

### ✍️ Completa el código que falta

**Objetivo:** Contar cuántos números del 1 al 20 son divisibles por 3.

```python
contador = 0

for i in range(1, ___):
    if i ___ 3 == ___:
        ___ += 1

print(f"Hay {contador} números divisibles por 3")
```

<details>
<summary>📋 Ver respuesta</summary>

```python
contador = 0

for i in range(1, 21):
    if i % 3 == 0:
        contador += 1

print(f"Hay {contador} números divisibles por 3")  # → 6
```

</details>

### 🔍 Encuentra el Error

```python
for i in range(1, 11):
    if i % 2 = 0:
        print(f"{i} es par")
```

<details>
<summary>📋 Ver respuesta</summary>

Se usa `=` (asignación) en vez de `==` (comparación):

```python
if i % 2 == 0:  # ← doble igual para comparar
```

</details>

---

# 🟦 NIVEL 5 — `break` y `continue`: Control del Flujo Interno

## 🎯 Concepto

| Palabra | Qué hace | Metáfora |
|---------|---------|----------|
| `break` | **Detiene** el ciclo completamente | Salir de la tienda 🚪 |
| `continue` | **Salta** a la siguiente vuelta | Saltarse una canción ⏭️ |

### `break` — Detener el ciclo

```python
for i in range(1, 11):
    if i == 6:
        print("¡Encontré el 6! Me detengo.")
        break
    print(i)
```

**Salida:**
```
1
2
3
4
5
¡Encontré el 6! Me detengo.
```

### `continue` — Saltar una vuelta

```python
for i in range(1, 11):
    if i % 2 == 0:
        continue  # salta los pares
    print(i)
```

**Salida:**
```
1
3
5
7
9
```

### 🌍 Ejemplo de la vida real: Buscar un producto en inventario

```python
productos = "ABCDEFGHIJ"  # códigos de 10 productos (como string)
buscado = input("¿Qué código buscas? ").upper()

for codigo in productos:
    if codigo == buscado:
        print(f"✅ Producto '{codigo}' encontrado")
        break
else:
    print("❌ Producto no encontrado")
```

> 💡 **Dato:** El `else` de un `for` se ejecuta solo si el ciclo terminó **sin** `break`.

### 🌍 Ejemplo: Validar contraseña con intentos limitados

```python
clave_correcta = "python123"

for intento in range(1, 4):
    clave = input(f"Intento {intento}/3 — Ingrese clave: ")
    if clave == clave_correcta:
        print("✅ Acceso concedido")
        break
else:
    print("🔒 Cuenta bloqueada")
```

---

## ✅ Chequeo de Comprensión — Nivel 5

### 🔘 Verdadero o Falso

| # | Afirmación | V/F |
|---|-----------|-----|
| 1 | `break` termina solo la vuelta actual del ciclo | |
| 2 | `continue` salta a la siguiente vuelta | |
| 3 | Después de un `break`, el ciclo nunca ejecuta más vueltas | |
| 4 | `continue` detiene el ciclo completo | |

<details>
<summary>📋 Ver respuestas</summary>

1. **FALSO** — `break` termina el ciclo COMPLETO
2. **VERDADERO** — Salta el resto del bloque y va a la siguiente vuelta
3. **VERDADERO** — El ciclo se detiene inmediatamente
4. **FALSO** — `continue` solo salta una vuelta, no detiene el ciclo

</details>

### 🔍 Encuentra el Error

```python
# Se quiere imprimir solo impares del 1 al 10
for i in range(1, 11):
    if i % 2 == 0:
        break
    print(i)
```

<details>
<summary>📋 Ver respuesta</summary>

Se usa `break` en vez de `continue`. Con `break`, el ciclo se detiene al primer par (2), así que solo imprime `1`:

```python
for i in range(1, 11):
    if i % 2 == 0:
        continue  # ← saltar, no detener
    print(i)
```

</details>

---

# 🟦 NIVEL 6 — `for` con Strings: Iteración Real

## 🎯 Concepto

Un string es una **secuencia de caracteres**. El `for` puede recorrerlo carácter por carácter.

```python
texto = "python"

for letra in texto:
    print(letra)
```

**Salida:**
```
p
y
t
h
o
n
```

### 🌍 Ejemplo de la vida real: Validar que una contraseña tenga un número

```python
clave = input("Crea tu contraseña: ")
tiene_numero = False

for caracter in clave:
    if caracter.isdigit():
        tiene_numero = True
        break

if tiene_numero:
    print("✅ Contraseña válida")
else:
    print("❌ Debe tener al menos un número")
```

### 🌍 Ejemplo: Contar vocales en un nombre

```python
nombre = input("Tu nombre: ")
vocales = 0

for letra in nombre.lower():
    if letra in "aeiou":
        vocales += 1

print(f"Tu nombre tiene {vocales} vocales")
```

### 🌍 Ejemplo: Censurar una palabra

```python
texto = input("Escribe una frase: ")
censurada = input("¿Qué letra censurar? ")
resultado = ""

for letra in texto:
    if letra.lower() == censurada.lower():
        resultado += "*"
    else:
        resultado += letra

print(f"Resultado: {resultado}")
```

**Ejemplo de ejecución:**
```
Escribe una frase: Hola Mundo
¿Qué letra censurar? o
Resultado: H*la Mund*
```

---

## ✅ Chequeo de Comprensión — Nivel 6

### 🔗 Términos Pareados

| # | Código | | Resultado |
|---|--------|-|-----------|
| A | `for c in "abc": print(c)` | | Imprime cada vocal del texto |
| B | `for c in texto: if c.isdigit(): ...` | | Imprime: a, b, c |
| C | `for c in texto: if c in "aeiou": ...` | | Detecta números en el texto |

<details>
<summary>📋 Ver respuestas</summary>

- A → Imprime: a, b, c
- B → Detecta números en el texto
- C → Imprime cada vocal del texto

</details>

### ✍️ Completa el código que falta

**Objetivo:** Contar cuántas letras mayúsculas hay en un texto.

```python
texto = "Hola Mundo Python"
contador = ___

for ___ in texto:
    if caracter.___():
        contador += 1

print(f"Hay {contador} mayúsculas")
```

<details>
<summary>📋 Ver respuesta</summary>

```python
texto = "Hola Mundo Python"
contador = 0

for caracter in texto:
    if caracter.isupper():
        contador += 1

print(f"Hay {contador} mayúsculas")  # → 3
```

</details>

---

# 🔤 Sopa de Letras — Conceptos del `for`

Busca las siguientes palabras en la sopa:

**Palabras:** `FOR`, `RANGE`, `BREAK`, `CONTINUE`, `ACUMULADOR`, `PASO`, `INICIO`, `STRING`, `ITERAR`, `CONTADOR`

```
C O N T I N U E R A
A C U M U L A D O R
B I T E R A R N G E
R N S T R I N G O T
E I F O R A N G E I
A C O N T A D O R C
K I N I C I O R P I
R O P A S O F O R N
A D O R A N G E S I
C O N T A D O R A P
```

<details>
<summary>📋 Ubicación de las palabras</summary>

- **CONTINUE** → Fila 1, horizontal →
- **ACUMULADOR** → Fila 2, horizontal →
- **ITERAR** → Fila 3, posición 3, horizontal →
- **STRING** → Fila 4, posición 4, horizontal →
- **FOR** → Fila 5, posición 3, horizontal →
- **CONTADOR** → Fila 6, posición 1, horizontal →
- **INICIO** → Fila 7, posición 2, horizontal →
- **PASO** → Fila 8, posición 4, horizontal →
- **RANGE** → Fila 9, posición 4, horizontal →
- **BREAK** → Columna 1, vertical ↓ (filas 3-7)

</details>

---

# 🏋️ Ejercicios de Práctica

## 🟢 Nivel Fácil (Para empezar)

### Ejercicio 1: Tabla de multiplicar
Pide un número al usuario y muestra su tabla de multiplicar del 1 al 10.

```
Entrada: 5
Salida esperada:
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
...
5 x 10 = 50
```

<details>
<summary>💡 Pista</summary>

Usa `range(1, 11)` y multiplica el número del usuario por `i`.

</details>

<details>
<summary>📋 Solución</summary>

```python
numero = int(input("Ingrese un número: "))

for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")
```

</details>

---

### Ejercicio 2: Repetir un mensaje
Pide al usuario un mensaje y un número. Imprime el mensaje esa cantidad de veces.

```
Entrada: mensaje = "Hola", veces = 3
Salida:
Hola
Hola
Hola
```

<details>
<summary>📋 Solución</summary>

```python
mensaje = input("Mensaje: ")
veces = int(input("¿Cuántas veces? "))

for _ in range(veces):
    print(mensaje)
```

</details>

---

### Ejercicio 3: Sumar N números
Pide al usuario cuántos números quiere sumar, luego pídelos uno por uno y muestra el total.

<details>
<summary>📋 Solución</summary>

```python
n = int(input("¿Cuántos números? "))
suma = 0

for i in range(1, n + 1):
    num = int(input(f"Número {i}: "))
    suma += num

print(f"Total: {suma}")
```

</details>

---

## 🟡 Nivel Medio (Integrando conceptos)

### Ejercicio 4: Números pares e impares
Muestra todos los números del 1 al N (ingresado por el usuario) indicando si cada uno es par o impar.

<details>
<summary>📋 Solución</summary>

```python
n = int(input("Ingrese N: "))

for i in range(1, n + 1):
    if i % 2 == 0:
        print(f"{i} → par")
    else:
        print(f"{i} → impar")
```

</details>

---

### Ejercicio 5: Promedio con nota mínima y máxima
Pide 5 notas, calcula el promedio, y muestra la nota más alta y más baja.

<details>
<summary>💡 Pista</summary>

Necesitas 3 variables: `suma`, `mayor` (inicia en 0), `menor` (inicia en un número alto como 100).

</details>

<details>
<summary>📋 Solución</summary>

```python
suma = 0
mayor = 0
menor = 100

for i in range(1, 6):
    nota = float(input(f"Nota {i}: "))
    suma += nota
    if nota > mayor:
        mayor = nota
    if nota < menor:
        menor = nota

promedio = suma / 5
print(f"\nPromedio: {promedio:.1f}")
print(f"Nota más alta: {mayor}")
print(f"Nota más baja: {menor}")
```

</details>

---

### Ejercicio 6: Triángulo de asteriscos
Imprime un triángulo rectángulo de altura N:

```
Entrada: 5
Salida:
*
**
***
****
*****
```

<details>
<summary>📋 Solución</summary>

```python
n = int(input("Altura: "))

for i in range(1, n + 1):
    print("*" * i)
```

</details>

---

### Ejercicio 7: Validar RUT (simplificado)
Recorre un string de RUT y verifica que todos los caracteres antes del guión sean dígitos.

```
Entrada: "12345678-9"
Salida: "✅ RUT válido"

Entrada: "123ab678-9"
Salida: "❌ RUT inválido"
```

<details>
<summary>📋 Solución</summary>

```python
rut = input("Ingrese RUT (sin puntos): ")
valido = True

for caracter in rut:
    if caracter == "-":
        break
    if not caracter.isdigit():
        valido = False
        break

if valido:
    print("✅ RUT válido")
else:
    print("❌ RUT inválido")
```

</details>

---

## 🟠 Nivel Difícil (Combinando todo)

### Ejercicio 8: Analizador de contraseña completo
Pide una contraseña y verifica que cumpla TODAS estas reglas:
- Al menos 8 caracteres de largo
- Al menos una letra mayúscula
- Al menos una letra minúscula
- Al menos un número

Muestra un reporte de qué reglas cumple y cuáles no.

<details>
<summary>📋 Solución</summary>

```python
clave = input("Crea tu contraseña: ")

tiene_mayuscula = False
tiene_minuscula = False
tiene_numero = False
largo_ok = len(clave) >= 8

for c in clave:
    if c.isupper():
        tiene_mayuscula = True
    elif c.islower():
        tiene_minuscula = True
    elif c.isdigit():
        tiene_numero = True

print("\n--- Reporte de contraseña ---")
print(f"{'✅' if largo_ok else '❌'} Al menos 8 caracteres ({len(clave)} caracteres)")
print(f"{'✅' if tiene_mayuscula else '❌'} Tiene mayúscula")
print(f"{'✅' if tiene_minuscula else '❌'} Tiene minúscula")
print(f"{'✅' if tiene_numero else '❌'} Tiene número")

if largo_ok and tiene_mayuscula and tiene_minuscula and tiene_numero:
    print("\n🔐 Contraseña FUERTE")
else:
    print("\n⚠️ Contraseña DÉBIL")
```

</details>

---

### Ejercicio 9: Mini cajero automático
Simula un cajero que permite 3 operaciones (depósito o retiro) y muestra el saldo final.

<details>
<summary>📋 Solución</summary>

```python
saldo = 10000
print(f"💰 Saldo inicial: ${saldo}")

for operacion in range(1, 4):
    print(f"\n--- Operación {operacion}/3 ---")
    tipo = input("¿Depositar (d) o Retirar (r)? ").lower()
    monto = int(input("Monto: $"))

    if tipo == "d":
        saldo += monto
        print(f"  ✅ Depósito de ${monto}")
    elif tipo == "r":
        if monto > saldo:
            print("  ❌ Fondos insuficientes")
            continue
        saldo -= monto
        print(f"  ✅ Retiro de ${monto}")
    else:
        print("  ❌ Opción no válida")

print(f"\n💰 Saldo final: ${saldo}")
```

</details>

---

### Ejercicio 10: Cifrado César básico
Recorre cada letra de un mensaje y desplázala 3 posiciones en el alfabeto.

```
Entrada: "hola"
Salida: "krod"
```

<details>
<summary>💡 Pista</summary>

Usa `ord()` para obtener el código ASCII de una letra y `chr()` para convertirlo de vuelta. La `a` es `ord('a')` = 97.

</details>

<details>
<summary>📋 Solución</summary>

```python
mensaje = input("Mensaje a cifrar: ").lower()
cifrado = ""
desplazamiento = 3

for letra in mensaje:
    if letra.isalpha():
        codigo = ord(letra) - ord('a')
        nuevo_codigo = (codigo + desplazamiento) % 26
        cifrado += chr(nuevo_codigo + ord('a'))
    else:
        cifrado += letra

print(f"Mensaje cifrado: {cifrado}")
```

</details>

---

## 🔴 Nivel Experto (Para los que dominan todo)

### Ejercicio 11: Detector de palíndromo
Determina si un texto ingresado es un palíndromo (se lee igual al derecho y al revés). Ignora mayúsculas y espacios.

```
Entrada: "Anita lava la tina"
Salida: "✅ Es palíndromo"
```

<details>
<summary>📋 Solución</summary>

```python
texto = input("Texto: ").lower()

# Crear versión sin espacios
limpio = ""
for c in texto:
    if c != " ":
        limpio += c

# Crear versión invertida
invertido = ""
for c in limpio:
    invertido = c + invertido

if limpio == invertido:
    print("✅ Es palíndromo")
else:
    print("❌ No es palíndromo")
```

</details>

---

### Ejercicio 12: Generador de patrón diamante
Genera un diamante de asteriscos de tamaño N (solo impares):

```
Entrada: 5
Salida:
    *
   ***
  *****
   ***
    *
```

<details>
<summary>📋 Solución</summary>

```python
n = int(input("Tamaño (impar): "))

# Mitad superior (incluye el centro)
for i in range(1, n + 1, 2):
    espacios = (n - i) // 2
    print(" " * espacios + "*" * i)

# Mitad inferior
for i in range(n - 2, 0, -2):
    espacios = (n - i) // 2
    print(" " * espacios + "*" * i)
```

</details>

---

### Ejercicio 13: Análisis completo de texto
Pide un texto al usuario y genera un reporte completo:
- Total de caracteres
- Total de letras
- Total de números
- Total de espacios
- Total de otros caracteres
- Total de vocales
- Total de consonantes
- Carácter más frecuente (sin contar espacios)

<details>
<summary>📋 Solución</summary>

```python
texto = input("Ingrese un texto: ")

letras = 0
numeros = 0
espacios = 0
otros = 0
vocales = 0
consonantes = 0

# Para encontrar el carácter más frecuente
max_caracter = ""
max_frecuencia = 0

for c in texto:
    if c == " ":
        espacios += 1
    elif c.isalpha():
        letras += 1
        if c.lower() in "aeiouáéíóú":
            vocales += 1
        else:
            consonantes += 1
    elif c.isdigit():
        numeros += 1
    else:
        otros += 1

    # Contar frecuencia (sin espacios)
    if c != " ":
        frecuencia = 0
        for otro in texto:
            if otro.lower() == c.lower():
                frecuencia += 1
        if frecuencia > max_frecuencia:
            max_frecuencia = frecuencia
            max_caracter = c

print("\n--- REPORTE DE TEXTO ---")
print(f"Total de caracteres: {len(texto)}")
print(f"Letras: {letras}")
print(f"  ├─ Vocales: {vocales}")
print(f"  └─ Consonantes: {consonantes}")
print(f"Números: {numeros}")
print(f"Espacios: {espacios}")
print(f"Otros: {otros}")
print(f"Carácter más frecuente: '{max_caracter}' ({max_frecuencia} veces)")
```

</details>

---

# 📊 Resumen Rápido — Cheat Sheet

```
┌──────────────────────────────────────────────────┐
│                  EL CICLO FOR                     │
├──────────────────────────────────────────────────┤
│                                                   │
│  for variable in secuencia:                       │
│      # bloque que se repite                       │
│                                                   │
├──────────────────────────────────────────────────┤
│  RANGE                                            │
│  range(fin)           → 0 hasta fin-1             │
│  range(inicio, fin)   → inicio hasta fin-1        │
│  range(ini, fin, paso)→ con saltos                │
│                                                   │
├──────────────────────────────────────────────────┤
│  CONTROL                                          │
│  break    → detiene el ciclo completo             │
│  continue → salta a la siguiente vuelta           │
│                                                   │
├──────────────────────────────────────────────────┤
│  ACUMULADORES                                     │
│  Suma:    variable = 0  →  variable += valor      │
│  Conteo:  variable = 0  →  variable += 1          │
│  Producto:variable = 1  →  variable *= valor      │
│  String:  variable = "" →  variable += caracter   │
│                                                   │
├──────────────────────────────────────────────────┤
│  STRINGS                                          │
│  for letra in "texto":                            │
│      # recorre carácter por carácter              │
│                                                   │
│  .isdigit()  .isalpha()  .isupper()  .islower()  │
│                                                   │
└──────────────────────────────────────────────────┘
```

---

# 🧪 Autoevaluación Final

Responde mentalmente antes de ver las respuestas:

1. ¿Qué genera `range(3, 12, 3)`?
2. ¿Cuál es la diferencia entre `break` y `continue`?
3. ¿Dónde se inicializa un acumulador, dentro o fuera del `for`?
4. ¿Qué pasa si escribo `range(5, 5)`?
5. ¿Puedo recorrer un string con `for`?
6. ¿Qué significa `_` como variable en un `for`?
7. ¿Qué método de string me dice si un carácter es un número?
8. ¿Qué imprime `for i in range(3): print(i)`?

<details>
<summary>📋 Ver todas las respuestas</summary>

1. `3, 6, 9` — empieza en 3, salta de 3 en 3, no llega a 12
2. `break` detiene todo el ciclo; `continue` salta solo la vuelta actual
3. **Fuera** del `for`, antes de que comience
4. No genera nada (secuencia vacía), el `for` no ejecuta ninguna vuelta
5. Sí, recorre cada carácter uno por uno
6. Significa "no me importa el valor, solo quiero repetir X veces"
7. `.isdigit()`
8. Imprime: `0`, `1`, `2` (en líneas separadas)

</details>
