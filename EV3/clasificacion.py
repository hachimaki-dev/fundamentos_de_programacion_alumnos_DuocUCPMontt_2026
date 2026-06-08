while True:
    try:
        cantidad = int(input("¿Cuantos alumnos hay?"))
        if cantidad > 0:
            break
        else:
            print("Ingrese un numero mayor a 0.")
    except ValueError:
        print("Entrada invalida.")
        
aprobados = 0
reprobados = 0

for i in range(cantidad):
    while True:
        try:
            nota =int(input(f"Ingrese su nota {i+1} "))
            if 1 <= nota <= 100:
                break
            print("la nota debe estar entre 1 y 100")
        except ValueError:
            print("Ingrese una nota entera valida")
            
            
if nota > 59:
    print("Aprobado")
    aprobados +=1
else:
    print("Repobrado")
    reprobados +=1
    
print(f"Resultado: {aprobados} y {reprobados} ")            