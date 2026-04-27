estudiantes = [
    {
        "nombre": "Dani Lobos",
        "edad": 28,
        "notas": [6.7, 5.0, 6.0]
    },
    {
        "nombre": "Cami Aravena",
        "edad": 28,
        "notas": [3.7, 5.0, 6.6]
    },
    {
        "nombre": "Max Salas",
        "edad": 30,
        "notas": [4.0, 3.0, 4.0]
    }
] 

for estudiante in estudiantes:
    suma = 0
    
    for nota in estudiante["notas"]:
        suma += nota
        
    promedio = suma /len(estudiante["notas"])
    
    print(estudiante["nombre"], "promedio", promedio)
    
    if promedio >= 4.0:
        print("APROBADO")
    else:
        print("REPROBADO")