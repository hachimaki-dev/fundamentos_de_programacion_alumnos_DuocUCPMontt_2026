# Saludo de bienvenida
# sin parámetros, sin return
# Crea una función mostrar_bienvenida() que no reciba nada y no retorne nada, solo imprima un mensaje de bienvenida a la biblioteca. Llámala 3 veces seguidas.

# 🤔 Pregúntate: ¿qué pasaría si guardas x = mostrar_bienvenida() y luego imprimes x? Pruébalo y reflexiona por qué da ese resultado.

def mostrarBienvenida():
    print("Bienvenida a la biblioteca")
    
x = mostrarBienvenida()
x = mostrarBienvenida()
x = mostrarBienvenida()
print(x)

#En el output aparecen tres veces seguidas el mensaje "Bienvenida a la biblioteca", sin embargo al final aparece "None", debido a que la función monstrarBienvenida() no retorna nada.