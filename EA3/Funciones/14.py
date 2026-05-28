def buscar_alumno(rut: str, students_dictionary: dict) -> str:
    for student in students_dictionary:
        if rut in students_dictionary.keys():
            return students_dictionary.get(rut)
        
    return "No encontrado"

print(buscar_alumno("1234",{"7890": "Martin"}))
print(buscar_alumno("1234",{"1234": "Obi-wan"}))