rut = []
menor = 0
mayor = 0


while True:
    try:
        pacientes =int(input("Cuantos pacientes se registraran hoy: "))
        if pacientes > 0:
            break
        else:
            print("Tiene que ser mayor a 0")
    except ValueError:
        print("¡ERROR TIENE QUE SER UN NUMERO!")
        
for i in range (pacientes):
    while True:
            rut_paciente = input("Ingrese su rut: ")
            if len(rut_paciente) == 9 and not " " in rut_paciente:
                rut.append(rut_paciente)
                break
            else:
                print("El rut del paciente debe llevar 9 caracteres y sin espacios")
                
    while True:
        try:
            edad = int(input("Ingrese su edad: "))
            if edad > 0:
                if edad < 18:
                    menor +=1
                    break
                else:
                    mayor +=1
                    break
                    
            else:
                print("Tiene que ser mayor a cero")
        except ValueError:
            print("¡ERROR TIENE QUE SER UN NUMERO!")
            
                    
print(f"La clinica registro {menor} pacientes menores y {mayor} pacientes adultos")

atencion = 40
capacidad = 40
reservas = 0

while True:
        print("== AGENDA CLINICA DENTAL SONRISA ==")
        print("1. Ver horas disponibles")
        print("2. Reservar hora(s)")
        print("3. Cancelar hora(s)")
        print("4. Ver reservas activas")
        print("5. Salir")
        opcion =input("Elija una opcion: ")
        
        if opcion == "1":   
            print(f"Los horarios disponibles son {atencion}")
            
        elif opcion == "2":
            while True:
                try:
                    cantidad = int(input("¿Cuántas horas reservar? "))
                    if cantidad <= 0:
                        print("Tiene que ser mayor a 0")
                    elif cantidad > atencion:
                        print(f"Error: solo hay {atencion} horas disponibles.")
                    else:
                        atencion -= cantidad
                        reservas += cantidad
                        print("Reserva registrada.")
                        break
                except ValueError:
                    print("Tiene que ser un número.")
                
        elif opcion == "3":
            while True:
                try:
                    cantidad =int(input("¿Cuantas horas desea cancelar?"))
                    if cantidad <= 0:
                        print("Tiene que ser mayor a 0")
                    elif cantidad > reservas:
                        print(f"Error: solo hay {reservas} horas disponibles.")
                    else:
                        atencion += cantidad    
                        reservas -= cantidad
                        
                        print("Reserva cancelada.")
                        break
                except ValueError:
                    print("Tiene que ser un número.")
                    
                    
        elif opcion == "4":
            print(f"Reservas activas: {reservas}")
                        
        elif opcion == "5":
            print("Hasta luego")
            break
        
        else: 
            print("Opcion invalida")
            
        
        
        
        
          
            
                    
                
            
            
        
        
    