def promedio(lista):
    if len(lista) == 0:
        return 0        
    return sum(lista) / len(lista)
print("Promedio lista vacía:", promedio([]))