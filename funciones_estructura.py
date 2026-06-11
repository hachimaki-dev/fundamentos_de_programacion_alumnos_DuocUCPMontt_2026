
def saludar():
    print("Saludo desde funcion")

saludar()
def saludar_con_retorno(catcher):
    return f"Saludo desde funcion {catcher} "
for i in range(1,4):
    respuesta = saludar_con_retorno(i)
    print(respuesta)