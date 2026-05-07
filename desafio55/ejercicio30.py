print("Situación: tu página web se cae y debes de hacer un script que sepa que hacer en ese momento.")
codigos = [200, 404, 500, 200, 500]
reintentos = 1
for code in codigos:
    if code == 200:
        print(f"Código número: {code} Ok")
    elif code == 404:
        print(f"Código número: {code} No encontrado.")
    elif code == 500:
        print(f"Código número: {code}, reintentando...")
        reintentos -= 1
        if reintentos == 0:
            print("Servidor Caido.")
            break
