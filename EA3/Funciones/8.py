def filtrar_pares(num_list: list) -> list:
    even_nums = []
    for num in num_list:
        if num % 2 == 0:
            even_nums.append(num)

    return even_nums

print(filtrar_pares([1,2,3,4,5,6,7,8,9]))