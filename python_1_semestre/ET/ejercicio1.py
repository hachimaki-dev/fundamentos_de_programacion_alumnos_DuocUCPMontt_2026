def sumar_numeros(numero1,numero2):
    return numero1 + numero2

suma_de_numeros = sumar_numeros(1,2)
print(suma_de_numeros)

def saludar(nombre , rol = "estudiante"):
    mensaje_de_saludo = f"HOLA {nombre} COMO ESTAS ? , tu rol es : {rol}"
    algo_mas = " son estudiantes de primer ano"
    return mensaje_de_saludo , algo_mas

saludo = saludar("JUAN y pedro")
print(saludo)

def aprobacion(promedio):
    if promedio >= 4.0:
        return "Felicidades aprobaste"
    return "reprobaste"

def sumarnotas(notas):
    total = sum(notas)
    cantidad = len(notas)
    return total / cantidad

notas_alumnos = [1.0,7.0,7.0]
promedio_final = sumarnotas(notas_alumnos)
aprobacion_promedio = aprobacion(promedio_final)
print(aprobacion_promedio)

