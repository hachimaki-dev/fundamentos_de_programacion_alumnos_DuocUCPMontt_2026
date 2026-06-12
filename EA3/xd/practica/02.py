# Duplicar: print vs return
# Concepto 1
# Crea dos funciones: duplicar_print(numero) que imprima el doble, y duplicar_return(numero) que lo retorne. Luego:

# a = duplicar_print(5)
# b = duplicar_return(5)
# print(a)
# print(b)
# 🤔 Pregúntate: ¿por qué a y b son distintos aunque ambas funciones «hacen lo mismo» a primera vista?

def duplicarPrint(numero):
    print(numero * 2)

def duplicarReturn(numero):
    return numero * 2

a = duplicarPrint(5)
b = duplicarReturn(5)
print(a)
print(b)

#"a" y "b" son diferentes, porque "a" invoca la función duplicarPrint(numero), la cual no retorna nada, solo imprime, por lo tanto además de mostrar el resultado, este retorna "None". En cambio, "b" sí tiene un return, entonces, la función duplicarReturn(numero) solo responde con el resultado de la multipicación.