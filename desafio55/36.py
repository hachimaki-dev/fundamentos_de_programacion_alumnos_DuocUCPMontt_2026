servidor1 = ["U1","U2"]
servidor2 = ["U2","U3"]
for i in servidor2:
    if i not in servidor1:
        servidor1.append(i)
print(servidor1)