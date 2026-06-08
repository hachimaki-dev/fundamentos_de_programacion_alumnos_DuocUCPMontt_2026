# Ejercicio 22 — Sistema de gestión de una clínica veterinaria

# 1. Preguntar cuántos animales se registrarán (entero positivo, validado)

# 2. Para cada animal:
# - ID del animal: mínimo 6 caracteres, sin espacios
# - Peso en kg: entero positivo, validado

# 3. Clasificar:
# - Peso > 25 kg → Paciente Grande
# - Peso ≤ 25 kg → Paciente Pequeño

#4. Al finalizar mostrar:
#"La clínica ha registrado X pacientes grandes e Y pacientes pequeños"
paciente_grandes_pequeños = {
    "pacientes_grande" : 0,
    "pacientes_pequeños" : 0
}
while True:
    try:
        cantidad_animales = int(input("Ingrese la cantidad de pacientes a ingresar \n"))
        if cantidad_animales <= 0:
            print("No puede ser un numero igual a 0 o negativo")
            continue
        for animales in range(cantidad_animales):
            id_cada_animal = str(input("Ingrese el ID del animal")).upper()
            if len(id_cada_animal) < 6 or " " in id_cada_animal:
                print("El ID del paciente debe tener 6 o mas caracteres y sin espacios entre medio")
                continue
            peso_del_animal_paciente = int(input("Ingrese el peso del animal"))
            if peso_del_animal_paciente <= 0:
                print("Peso no debe ser 0 o un numero negativo")
                continue
            if peso_del_animal_paciente > 25:
                print("Paciente grande")
                paciente_grandes_pequeños["pacientes_grande"] += 1
            elif peso_del_animal_paciente <= 25:
                print("Paciente pequeño")
                paciente_grandes_pequeños["pacientes_pequeños"] += 1
        print(f"La clinica ha registrado {paciente_grandes_pequeños["pacientes_grande"]} pacientes grandes y {paciente_grandes_pequeños["pacientes_pequeños"]} pacientes pequeños")
        break
    except Exception as error:
        print(f"ERROR : {error}")