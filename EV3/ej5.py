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
    product_code = input("Ingresa el código del producto: ")

    if rule_length(product_code, 6) and rule_no_spaces(product_code):
        break
    else:
        print("Nombre de código inválido. Debe tener al menos 6 caracteres y no contener espacios.")
        
print(f"Producto registrado con código: {product_code}")