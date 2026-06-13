#sin retorno

def saludarCompi():
    print("hola")

def saludarCompiConParametr(nombre_del_compi):
    print(f"hola {nombre_del_compi}")

saludarCompi()

#con retorno
contador = 0
def saludarCompi():
    return "hola"

def saludarCompiConParametr(nombre_del_compi):
    return nombre_del_compi

guardando_respuesta = saludarCompi()

print(f"esta es la respues: {guardando_respuesta}")