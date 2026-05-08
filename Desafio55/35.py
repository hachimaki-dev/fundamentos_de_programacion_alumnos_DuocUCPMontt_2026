transferencias_del_dia=[15000, 80000, 2000, 150000]
importantes=[]
for x in transferencias_del_dia:
    if x>=50000:
        importantes.append(x)
print(importantes)