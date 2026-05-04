#ejercicio1
saludo = "Hola Mundo"
print(saludo)

#ejercicio2
total = (15 + 25) * 2
print(total)

#ejercicio3
nota = float(input("Ingrese su nota "))
estado = ""
if nota >= 4.0:
    estado = "Aprobado"
    print(estado)
elif nota < 4.0:
    estado = "Reprobado"
    print(estado)
else:
    print("la nota no es valida")
