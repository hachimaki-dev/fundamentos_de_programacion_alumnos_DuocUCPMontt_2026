servidor1=["U1", "U2"]
servidor2=["U2", "U3"]
sevidor_combinado=[]
for i in servidor1:
    sevidor_combinado.append(i)
for x in servidor2:
    if x not in servidor1:
        sevidor_combinado.append(x)
print((sevidor_combinado))