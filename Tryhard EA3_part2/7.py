#Ejercicio 7 — Crear y recorrer una lista de diccionarios
#Contexto: Registro de pacientes en clínica.
#Lo que debe hacer el programa: Pide los datos de exactamente 3 pacientes: nombre (que no esté vacío) y edad (entero positivo).
#Guarda cada paciente en una lista, como si fuera una ficha. Al terminar, muestra la lista completa con el nombre y edad de cada uno.

pacientes=[]
for i in range(3):
    print(f"\n--- Registrar Paciente {i+1} ---")
    while True:
        nombre=input("\nPor favor ingrese el nombre del paciente: ").strip()
        if len(nombre)>0:
            break
        print("El nombre no puede estar vacio")

    while True:
        try:
            edad=int(input("Por favor ingrese la edad del paciente: "))
            if edad>0:
                break
            print("La edad debe ser mayor a 0")
        except ValueError:
            print("Por favor ingese un numero entero")

    paciente={"nombre": nombre, "edad": edad}
    pacientes.append(paciente)
print("\n--- Lista de pacientes---")
for p in pacientes:
    print(f"Nombre {p['nombre']} | Edad {p['edad']}")