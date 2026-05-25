servidor1 = ["U1", "U2"]
servidor2 = ["U2", "U3"]

for usuarios in servidor2:
    if usuarios not in servidor1:
        servidor1.append(usuarios)
print(servidor1)