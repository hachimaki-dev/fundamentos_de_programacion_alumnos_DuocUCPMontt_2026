respuestas=["Juan",None,"Ana",""]
limpio=[]

for i in respuestas:
    if i is not None:
        nombres=i.strip()

        if nombres != "":
            limpio.append(nombres)

print(limpio)