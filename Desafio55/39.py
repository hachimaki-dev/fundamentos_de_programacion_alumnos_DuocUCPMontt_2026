nombres = ['Juan', None, '', 'Ana', ' ']
real_names = []
for nombre in nombres:
    if nombre is not None and nombre.strip() != '':
        real_names.append(nombre.strip())

print(real_names)