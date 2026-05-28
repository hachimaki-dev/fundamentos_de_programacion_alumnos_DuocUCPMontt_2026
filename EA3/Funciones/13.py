def promedio(num_list: list) -> int | float:
    if len(num_list) == 0:
        return 0
    
    nums = 0

    for num in num_list:
        nums += num

    return nums / len(num_list)

print(promedio([2,2,2,2]))
print(promedio([]))
print(promedio([2,6,8,4,8]))