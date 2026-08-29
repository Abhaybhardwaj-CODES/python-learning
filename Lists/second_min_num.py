List = [1, 9, 6, 3, 0]

min_num = List[0]
second_num = List[0]

for i in range(1, len(List)):
    if List[i] < min_num:
        second_num = min_num
        min_num = List[i]

    elif List[i] < second_num:
        second_num = List[i]

print(f"The second max number is: {second_num}")