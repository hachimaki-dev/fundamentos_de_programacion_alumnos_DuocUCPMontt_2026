Servidor = ["U1" , "U2"]
Servidor_2 = ["U2" , "U3"]

for i in Servidor_2:

    if i not in Servidor:
        Servidor.append("U3")

print (Servidor)