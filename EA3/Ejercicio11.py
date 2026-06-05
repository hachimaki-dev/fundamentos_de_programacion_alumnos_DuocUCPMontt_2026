def contar_caracteres(texto):
    resultado = {}
    for i in texto:
        if i not in resultado:
            resultado[i]= 1
        elif i in resultado:
            resultado[i]+=1
    return(resultado)

print(contar_caracteres("Hola a todos"))
    
        