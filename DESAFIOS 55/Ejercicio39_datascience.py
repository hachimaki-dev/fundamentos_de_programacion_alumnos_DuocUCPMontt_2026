data=['Juan', None, '', 'Ana', ' ']
datalimpia=[]
for i in data:
    if i is not None and i.strip()!= '':
        datalimpia.append(i.strip())
print(datalimpia)        