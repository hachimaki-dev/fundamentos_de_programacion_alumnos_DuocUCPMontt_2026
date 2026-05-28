def rule_exact_length(text: str, length: int) -> bool:
    if len(text) == length:
        return True
    else:
        return False
    
def rule_no_spaces(text: str) -> bool:
    if text.count(" ") >= 1:
        return False
    else:
        return True
    
while True:
    plate = input("Ingresa la patente: ")

    if rule_exact_length(plate, 6) and rule_no_spaces(plate):
        break
    else:
        print("Patente inválida. Debe tener exactamente 6 caracteres y no contener espacios.")
        
print(f"Patente registrada: {plate}")