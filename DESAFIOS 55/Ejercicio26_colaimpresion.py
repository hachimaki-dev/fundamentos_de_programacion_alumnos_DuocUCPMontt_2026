papel=5
cola=['TEXTO','FOTO','TEXTO','FOTO']

for i in cola:
    

    
    if papel==0:
        print ('Sin papel')
        break
    
        
    if i == 'TEXTO':
        papel -= 1
    elif i == 'FOTO':
        papel -= 3    
    print (f'Imprimiento {i}')