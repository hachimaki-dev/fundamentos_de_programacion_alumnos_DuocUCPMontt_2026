import secrets
import string
def generar_password(longitud=8):
    return "".join(secrets.choice(string.ascii_letters + string.digits) for i in range(longitud))