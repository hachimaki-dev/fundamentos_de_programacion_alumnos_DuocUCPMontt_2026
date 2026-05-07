servidor1 = ["U1", "U2"]
servidor2 = ["U2", "U3"]

for user in servidor2:
    if user not in servidor1:
        servidor1.append(user)
        
print(servidor1)