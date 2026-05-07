servidor_1 = ["U1","U2"]
servidor_2 = ["U2","U3"]

for i in servidor_2 :
    
    if servidor_2[0] not in servidor_1 :
        
        servidor_1.append(servidor_2)
        
    else: 
        servidor_1.pop(1)



print(servidor_1)