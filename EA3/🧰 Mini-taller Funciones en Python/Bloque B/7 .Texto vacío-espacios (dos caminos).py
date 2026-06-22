def tiene_contenido_v1(texto):
    for caracter in texto:
        if caracter != " ":
            return True
    
    return False

print()

print(tiene_contenido_v1(" "))
print(tiene_contenido_v1(""))
print(tiene_contenido_v1(" Don Quijote "))


print()
print("Tiene_contenido_V2")

def tiene_contenido_v2(texto):
    return texto.strip() != ""

print(tiene_contenido_v2(" "))
print(tiene_contenido_v2(""))
print(tiene_contenido_v2(" Don Quijote "))

# "   Don Quijote   "
#  ^               ^
#  |               |
# lstrip()      rstrip()

# strip() quita ambos lados
