# TERMINADO

alumnos = ["Harry", "Hermione", "Ron", "Draco", "Neville", "Luna"]

gryffindor = [] 
slytherin = []
contador = 0

for alumno in alumnos:
    print(f"alumno {contador} longitud de nombre  {len(alumno)}")

    if len(alumno) > 5:
        gryffindor.append(alumno)

    else:
        slytherin.append(alumno)
    
    contador += 1


print("-" * 30) 
print(f"RESULTADO FINAL GRYFFINDOR: {gryffindor}")
print(f"RESULTADO FINAL SLYTHERIN: {slytherin}")
print("-" * 30) 