def espar(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

for i in range(1, 101):
    print(f"{i} = {espar(i)}")