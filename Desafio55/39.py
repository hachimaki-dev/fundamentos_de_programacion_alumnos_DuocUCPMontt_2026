respuestas=["Juan", None, "", "Ana", " "]
respuestas_validas=[]
for x in respuestas:
    if x is not None and x.strip()!="":
        respuestas_validas.append(x)
print(respuestas_validas)