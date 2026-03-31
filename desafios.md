
🧠 Evaluación Parcial 1 – Fundamentos de Programación (Python)
Duración: 2 horas
Modalidad: Individual
Lenguaje: Python

🎯 Objetivo evaluativo
Evaluar la capacidad del estudiante para:

Modelar problemas en código.

Aplicar estructuras de decisión (if) y repetición (while).

Manejar variables, contadores y acumuladores.

Diseñar lógica coherente y legible.

🔹 EJERCICIO 1 (41 puntos)
🔍 Control de acceso (estructura condicional)
📘 Enunciado (versión Pythonizada y clara)
Desarrolle un programa en Python que permita validar si una persona puede inscribirse en un taller.

El programa debe:

Solicitar la edad (entero).

Solicitar si está inscrita previamente (SI / NO).

📏 Reglas:
Si edad ≥ 18:

Si respondió "SI" → mostrar: Inscripción aceptada

En otro caso → mostrar: Inscripción rechazada

Si edad < 18:

Mostrar: Debe ser mayor de edad para poder inscribirse

📤 Salida obligatoria:
Siempre mostrar al final:

Fin del proceso
🧩 Ejemplo de ejecución
Ingrese edad: 20
¿Está inscrito previamente? SI

Inscripción aceptada
Fin del proceso
🧮 Pauta de evaluación (41 pts)
Criterio	Descripción	Puntos
Entrada de datos	Uso correcto de input() y conversión de tipos	6
Estructura condicional principal	Correcta evaluación de edad	10
Condición anidada	Uso correcto de condición interna (SI/NO)	10
Mensajes correctos	Coinciden exactamente con lo solicitado	5
Flujo lógico completo	No hay caminos sin cubrir	5
Cierre del programa	Muestra “Fin del proceso” siempre	5
🧠 Qué se evalúa realmente (pedagogía)
Aquí no se evalúa “si funciona”, sino:

Jerarquía de decisiones (if anidados)

Modelamiento de reglas de negocio

Control de flujo completo

💡 Ejemplo de solución esperada (referencial)
edad = int(input("Ingrese edad: "))
inscrito = input("¿Está inscrito previamente? (SI/NO): ")

if edad >= 18:
    if inscrito == "SI":
        print("Inscripción aceptada")
    else:
        print("Inscripción rechazada")
else:
    print("Debe ser mayor de edad para poder inscribirse")

print("Fin del proceso")
🔹 EJERCICIO 2 (59 puntos)
🔁 Sistema con menú + acumulación
📘 Enunciado
Desarrolle un programa en Python que permita registrar actividades diarias y analizar el tiempo total.

⚙️ Requisitos funcionales
🟢 Menú principal (repetitivo)
Debe mostrarse hasta que el usuario elija salir:

1. Registrar actividades
2. Mostrar análisis del tiempo
3. Salir
🔹 Opción 1: Registrar actividades
Solicitar cantidad de actividades (≥ 3)

Usar:

contador

acumulador

Por cada actividad:

nombre

tiempo en minutos

Acumular el tiempo total

🔹 Opción 2: Análisis
Mostrar tiempo total

Si total > 180:

Tiempo diario excesivo

Si no:

Tiempo diario adecuado

🔹 Opción 3: Salir
Fin del registro
🧩 Ejemplo de ejecución
Registro de actividades diarias

1. Registrar actividades
2. Mostrar análisis del tiempo
3. Salir

Seleccione opción: 1
Cantidad: 3

Actividad: Estudiar
Tiempo: 120

Actividad: Comer
Tiempo: 30

Actividad: Ejercicio
Tiempo: 60
🧮 Pauta de evaluación (59 pts)
Criterio	Descripción	Puntos
Menú con while	Repetición correcta hasta salir	10
Validación de opción	Manejo correcto de entradas	5
Registro de actividades	Uso correcto de ciclo	10
Contador	Incremento correcto	5
Acumulador	Suma correcta del tiempo	10
Separación lógica	Menú vs procesamiento	5
Análisis condicional	Evaluación correcta del total	7
Persistencia de datos	No perder acumulado entre ciclos	5
Salida correcta	Finalización limpia	2
🧠 Qué se evalúa realmente
Este ejercicio mide:

Pensamiento algorítmico sostenido

Estado del programa (memoria entre iteraciones)

Diferencia entre flujo interactivo y cálculo

💡 Ejemplo de solución esperada
total_tiempo = 0

while True:
    print("\nRegistro de actividades diarias")
    print("1. Registrar actividades")
    print("2. Mostrar análisis del tiempo")
    print("3. Salir")

    opcion = int(input("Seleccione opción: "))

    if opcion == 1:
        cantidad = int(input("Cantidad de actividades (>=3): "))
        contador = 0

        while contador < cantidad:
            nombre = input("Nombre actividad: ")
            tiempo = int(input("Tiempo en minutos: "))

            total_tiempo += tiempo
            contador += 1

    elif opcion == 2:
        print("Tiempo total:", total_tiempo)

        if total_tiempo > 180:
            print("Tiempo diario excesivo")
        else:
            print("Tiempo diario adecuado")

    elif opcion == 3:
        print("Fin del registro")
        break
🔥 Mejora pedagógica clave (esto es lo importante)
Lo que hicimos aquí —y que te recomiendo adoptar como estándar—:

1. Separar claramente:
qué hace el programa

cómo se evalúa

qué competencia mide

2. Evaluar pensamiento, no solo resultado
Ahora puedes detectar:

estudiantes que copian vs entienden

errores conceptuales (no solo sintácticos)

3. Hacer visible el criterio
El estudiante sabe:

qué vale puntos

por qué pierde puntos