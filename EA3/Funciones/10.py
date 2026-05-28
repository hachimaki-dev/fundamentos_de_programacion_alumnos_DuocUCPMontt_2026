import string
import secrets

def generar_password(length: int=8) -> str:
    characters = string.ascii_letters + string.digits + string.punctuation

    password = "".join(secrets.choice(characters) for _ in range(length))

    return password

print(generar_password())
print(generar_password(50))