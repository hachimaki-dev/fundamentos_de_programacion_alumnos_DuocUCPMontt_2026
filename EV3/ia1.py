aprobados = 0
reprobados = 0
promedio = 0

while True:
    try:
        n = int(input("¿Cuantos estudiantes se registraran?: "))
        if n <= 0:
            print("Error debe ser un numero positivo")
        else:
            break
    except ValueError:
        print("Error ingrese un numero entero")

for i in range(n):
    print(f"\n--- Estudiantes {i+1} ---")
    
    while True:
        codigo = input("Escriba su rut: ")
        if len(codigo) != 9:
            print("Error el rut es de 9 digitos")
        elif " " in codigo:
            print("Error el rut no puede tener espacios")
        else:
            break
        
    while True:
        try:
            promedio = int(input("Ingrese su promedio de notas: "))
            if promedio <= 0:
                print("Error el promedio debe ser positivo")
            elif promedio >= 60:
                print("Aprobaste")
                aprobados +=1
            else:
                print("Reprobaste")
                reprobados +=1
            break
        except ValueError:
            print("Ingrese un numero entero")
                
            
        
print(f"el instituo registro {aprobados} estudiantes aprobados y {reprobados} estudiantes reprobados. Proceso finalizado")
        
            
            
        
          
            