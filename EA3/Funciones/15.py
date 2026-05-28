def filtrar_pares(num_list: list[int | float]) -> list:
    even_nums = []
    for num in num_list:
        if num % 2 == 0:
            even_nums.append(num)

    return even_nums

def sumar_lista(nums_list: list) -> int | float:
    total = 0
    for num in nums_list:
        total += num

    return total

def sumar_pares_lista(num_list: list[int | float]) -> int | float:
    evens_list = filtrar_pares(num_list)
    return sumar_lista(evens_list)

print(sumar_pares_lista([1,5,8,3,9,2,67,126,48,23654878,1362472,163234]))