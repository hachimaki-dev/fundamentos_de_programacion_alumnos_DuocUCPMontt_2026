def promedio(lista : list=[]):
    total = 0 
    for i in lista:
        total +=i
    if len(lista)> 0:
        promedio= total/(len(lista))
    else:
        promedio = 0 
    return promedio
resultado = promedio([12,54,61,53,31,41,32])
print(resultado)