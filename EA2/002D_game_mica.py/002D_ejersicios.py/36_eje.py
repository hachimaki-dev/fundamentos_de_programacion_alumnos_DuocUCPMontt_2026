
servidor1 = ["u1" , "u2"]
servidor2 = ["u2" , "u3"]

for usuarios in servidor2:
    if usuarios not in servidor1:
        print(usuarios)