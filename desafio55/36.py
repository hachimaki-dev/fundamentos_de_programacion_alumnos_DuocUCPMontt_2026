usuarios_servidor1 = [ "U1", "U2" ]
usuarios_servidor2 = [ "U2", "U3" ]

for i in usuarios_servidor2:
    if i not in usuarios_servidor1:
        usuarios_servidor1.append(i)
    else:
        pass

print(usuarios_servidor1)
