servidor1 = ["U1", "U2"]
servidor2 = ["U2", "U3"]

for servidor in servidor2:
    if servidor not in servidor1:
        servidor1.append(servidor)
print(servidor1)