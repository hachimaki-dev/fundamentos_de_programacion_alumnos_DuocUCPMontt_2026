def rule_length(text: str, length: int) -> bool:
    if len(text) >= length:
        return True
    else:
        return False
    
def rule_no_spaces(text: str) -> bool:
    if text.count(" ") >= 1:
        return False
    else:
        return True

while True:
    username = input("Ingresa tu nombre de usuario: ")

    if rule_length(username, 6) and rule_no_spaces(username):
        break
    else:
        print("Nombre inválido. Debe tener al menos 6 caracteres y no contener espacios.")

print(f"Usuario creado: {username}")