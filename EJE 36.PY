servidor1 = ["U1", "U2"]
servidor2 = ["U2", "U3"]
 
for usuario in servidor2:
    if usuario not in servidor1:
        servidor1.append(usuario)
 
print(servidor1)
print()