#Fuck JK ROWLING
alumnos = ["Harry", "Hermione", "Ron", "Draco", "Neville", "Luna"]
gryffindor =[]
slytherin =[]

for i in alumnos:
    if len(i) > 5:
        gryffindor.append(i)
    else:
        slytherin.append(i)   

print("Gryffindor:")
for n in gryffindor:
    print(n) 
print("Slytherin: ")
for n in slytherin:
    print(n)